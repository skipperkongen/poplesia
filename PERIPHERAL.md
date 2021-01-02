# Capture data from your own computer

Your computer probably has both a camera and a microphone. You can capture and analyse data from these
using 3rd-party Python libraries as I've done in a [previous demo](https://github.com/skipperkongen/alarm-on-your-laptop).

- Capture a [single image](https://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python)
- Capture [audio](https://realpython.com/python-speech-recognition/)


### Python demo

Install dependencies in virtual environment:

```
python3 -m venv venv
source venv/bin/activate
# Installing takes several minutes...
pip install -r requirements.txt
```

Run demo program:

```
python ./demos/peripheral_demo.py
```

After running the program, you will have an image file (capture.jpg) and a data file (capture.json).

`capture.jpg`:

![](./capture_example.jpg)

`capture.json`:

```
{
  "type": "poplesia/capture/v0.0.1"
  "timestamp": 1609600389,
  "location": {
    "city": "Copenhagen",
    "region": "Capital Region",
    "country": "DK",
    "timezone": "Europe/Copenhagen",
    "ip": "<hidden>",
    "hostname": "<hidden>",
    "loc": "<hidden>",
    "org": "<hidden>",
    "postal": "<hidden>",
    "readme": "<hidden>"
  },
  "data": [
    {
      "type": "human/speech",
      "data": "I would like a cup of tea please"
    },
    {
      "type": "human/face_encoding",
      "data": [-0.01993358, 0.12578386, -0.03805061, ..., 0.06232701]
    }
  ]
}
```
