#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
print(sr.Microphone.list_working_microphones())
for device_index in sr.Microphone.list_working_microphones():
    print(device_index)
    m = sr.Microphone(device_index=device_index)
    break
else:
    print("No working microphones found!")

# obtain audio from the microphone
r = sr.Recognizer()
with m as source:
    print("Say something!")
    audio = r.listen(source)
    print("waiting")

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio,language='ru-RU'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))