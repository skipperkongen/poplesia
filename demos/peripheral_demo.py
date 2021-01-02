import json
import time

import cv2
import face_recognition as fr
import speech_recognition as sr
import imageio
import requests

recog = sr.Recognizer()

# Record from microphone
with sr.Microphone() as microphone:
        print('Adjusting for ambient noise')
        recog.adjust_for_ambient_noise(microphone)
        print('Please say something now...')
        audio = recog.listen(microphone)
        spoken = recog.recognize_google(audio, language='EN-us')
        print('Audio capture complete')

# Record from camera
print("Initialising camera")
cam = cv2.VideoCapture(0)
print('Please look into the camera...')
for i in range(3,0,-1):
  print(i)
  time.sleep(1)
ret, frame = cam.read()

print('Image capture complete')
print('Resizing image')
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
print('Converting the image from BGR color (OpenCV) to RGB color (face_recognition)')
rgb_small_frame = small_frame[:, :, ::-1]
print('Detecting faces')
face_locations = fr.face_locations(rgb_small_frame)
face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

print('Detecting location from IP')
resp = requests.get('https://ipinfo.io')
if resp.status_code == 200:
    print('Location detected')
    loc = resp.json()
else:
    loc = None
    print('Warning: device not online')

print('Storing information on disk')
imageio.imwrite('capture.jpg', frame)
capture_json = {
    'type': 'poplesia/capture/v0.0.1',
    'timestamp': int(time.time()),
    'location': loc,
    'data': []
}

if spoken:
    capture_json['data'].append({
        'type': 'human/speech',
        'data': spoken
    })
for face_encoding in face_encodings:
    capture_json['data'].append({
        'type': 'human/face_encoding',
        'data': face_encoding.tolist()
    })
with open('capture.json', 'w') as capture_file:
    json.dump(capture_json, capture_file)
print('Wrote capture to disk')

print()
print('Summary:')
print(f'- Speech detected: {spoken}')
print(f'- Faces detected: {len(face_encodings)}')
print(f'- Location detected: {loc is not None}')
