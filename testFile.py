import crepe
from scipy.io import wavfile
import aubio


'''
THIS IS CURRENTLY JUST PLACEHELD INFORMATION, BUT WITH
THE GIVEN VALUES BELOW, IT CAN BE USED TO MANIPULATE THE
FREQUENCY DATA OF THE SONG AND BE CHANGED INTO A CERTAIN
KEY, SUCH AS A#, C, D, ETC.

THIS COULD BE USED LATER TO FIND TIMES WHEN PLAYING MUSIC
AND MATCH THE NOTE TO THE SPECIFIC TIMESTAMP
'''
'''
This is just a placeholder incase it's hard to see the progression of the notesfrequency.
The actual chat that is used is below this one.
'''

# noteFrequencies = {"A0":  27.500, "A1":  55.000, "A2":  110.00, "A3":  220.00, "A4":  440.00, "A5":  880.00, "A6":  1760.0, "A7":  3520.0,
#                    "A0#": 29.135, "A1#": 58.270, "A2#": 116.54, "A3#": 233.08, "A4#": 466.16, "A5#": 932.33, "A6#": 1864.7, "A7#": 3729.3,
#                    "B0":  30.868, "B1":  61.735, "B2":  123.47, "B3":  246.94, "B4":  493.88, "B5":  987.77, "B6":  1975.5, "B7":  3951.1,
#                    "C1":  32.703, "C2":  65.486, "C3":  130.81, "C4":  161.63, "C5":  523.25, "C6":  1046.5, "C7":  2093.0, "C8":  4186.0,
#                    "C1#": 34.648, "C2#": 69.296, "C3#": 138.59, "C4#": 277.18, "C5#": 554.37, "C6#": 1108.7, "C7#": 2217.5,
#                    "D1":  36.708, "D2":  73.416, "D3":  146.83, "D4":  293.67, "D5":  587.33, "D6":  1174.7, "D7":  2349.3,
#                    "D1#": 38.891, "D2#": 77.782, "D3#": 155.56, "D4#": 311.13, "D5#": 622.25, "D6#": 1244.5, "D7#": 2489.0,
#                    "E1":  41.203, "E2":  82.407, "E3":  164.81, "E4":  329.63, "E5":  659.26, "E6":  1318.5, "E7":  2637.0,
#                    "F1":  43.654, "F2":  87.307, "F3":  174.61, "F4":  349.23, "F5":  698.46, "F6":  1396.9, "F7":  2793.0,
#                    "F1#": 46.249, "F2#": 92.499, "F3#": 185.00, "F4#": 369.99, "F5#": 739.99, "F6#": 1480.0, "F7#": 2960.0,
#                    "G1":  48.999, "G2":  97.999, "G3":  196.00, "G4":  392.00, "G5":  783.99, "G6":  1568.0, "G7":  3136.0,
#                    "G1#": 51.913, "G2#": 103.83, "G3#": 207.65, "G4#": 415.30, "G5#": 830.61, "G6#": 1661.2, "G7#": 3322.4}

sr, audio = wavfile.read("coconut.wav")
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)


notes = []

for freq in frequency:
    noteFrequency = aubio.freq2note(freq)
    notes.append(noteFrequency)


print(notes)
print("\n\n\n")
print(len(notes), len(frequency))
print(frequency[10], notes[10], "\n", \
      frequency[105], notes[105], "\n", \
      frequency[541], notes[541], "\n")
        