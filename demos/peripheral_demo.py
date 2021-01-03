import json
import time
import uuid

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
        from_timestamp = int(time.time())
        audio = recog.listen(microphone)
        to_timestamp = int(time.time())
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
    network_loc = resp.json()
else:
    network_loc = None
    print('Warning: device not online')

print('Storing information on disk')
imageio.imwrite('capture_peripheral.jpg', frame)

captures = []

if spoken:
    capture = {
        'id': str(uuid.uuid4()),
        'type': 'poplesia/types/audio_capture',
        'timestamp': from_timestamp,
        'agent': {
            'id': str(uuid.uuid4()),
            'type': 'microphone',
            'spec': 'MacBook Pro (15-inch, 2017)',
            'location': network_loc
        },
        'text': spoken
    }
    captures.append(capture)

for face_encoding in face_encodings:
    capture = {
        'id': str(uuid.uuid4()),
        'type': 'poplesia/types/face_capture',
        'timestamp': from_timestamp,
        'agent': {
            'type': 'camera',
            'id': str(uuid.uuid4()),
            'location': network_loc,
        },
        'face_encoding_128': face_encoding.tolist()
    }
    captures.append(capture)

with open('capture_peripheral.json', 'w') as capture_file:
    for capture in captures:
        capture_file.write(f'{json.dumps(capture)}\n')
print('Wrote capture to disk')

print()
print('Summary:')
print(f'- Speech detected: {spoken}')
print(f'- Faces detected: {len(face_encodings)}')
print(f'- Location detected: {network_loc is not None}')
