import librosa
import sys
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import sys
from aubio import source, pitch

np.set_printoptions(threshold=sys.maxsize)

filename = 'TuvanThroatSinging.wav'

win_s = 4096
hop_s = 512 

s = source(filename)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []

total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitches += [pitch]
    confidence = pitch_o.get_confidence()
    confidences += [confidence]
    total_frames += read
    if read < hop_s: break

count = 0
for pitch in pitches:
    count += 1
    if pitch != 0:
        print(librosa.hz_to_note(pitch))
    if count % 20 == True:
        break


print("Average frequency = " + str(np.array(pitches).mean()) + " hz")