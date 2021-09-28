import crepe
import pandas
from scipy.io import wavfile

'''
THIS IS CURRENTLY JUST PLACEHELD INFORMATION, BUT WITH
THE GIVEN VALUES BELOW, IT CAN BE USED TO MANIPULATE THE
FREQUENCY DATA OF THE SONG AND BE CHANGED INTO A CERTAIN
KEY, SUCH AS A#, C, D, ETC.

THIS COULD BE USED LATER TO FIND TIMES WHEN PLAYING MUSIC
AND MATCH THE NOTE TO THE SPECIFIC TIMESTAMP
'''


# file name is stored without extention
fileName = "coconut"

try:
    '''
    will try to read the file as a csv file
    '''
    
    df = pandas.read_csv(fileName + '.f0.csv')
except:
    '''
    will create a csv file from a wav file then read the csv file
    '''

    sr, audio = wavfile.read(fileName + '.wav')
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)

    '''
    This is just a placeholder incase it's hard to see the progression of the notesfrequency.
    The actual chat that is used is below this one.
    '''

    noteFrequencies = {"A0": 27.500, "A0#": 29.135, "B0": 30.868, "C1": 32.703, "C1#": 34.648, "D1": 36.708, "D1#": 38.891, "E1": 41.203, "F1": 43.654, "F1#": 46.249, "G1": 48.999, "G1#": 51.913,
                    "A1": 55.000, "A1#": 58.270, "B1": 61.735, "C2": 65.486, "C2#": 69.296, "D2": 73.416, "D2#": 77.782, "E2": 82.407, "F2": 87.307, "F2#": 92.499, "G2": 97.999, "G2#": 103.83,
                    "A2": 110.00, "A2#": 116.54, "B2": 123.47, "C3": 130.81, "C3#": 138.59, "D3": 146.83, "D3#": 155.56, "E3": 164.81, "F3": 174.61, "F3#": 185.00, "G3": 196.00, "G3#": 207.65,
                    "A3": 220.00, "A3#": 233.08, "B3": 246.94, "C4": 261.63, "C4#": 277.18, "D4": 293.67, "D4#": 311.13, "E4": 329.63, "F4": 349.23, "F4#": 369.99, "G4": 392.00, "G4#": 415.30,
                    "A4": 440.00, "A4#": 466.16, "B4": 493.88, "C5": 523.25, "C5#": 554.37, "D5": 587.33, "D5#": 622.25, "E5": 659.26, "F5": 698.46, "F5#": 739.99, "G5": 783.99, "G5#": 830.61,
                    "A5": 880.00, "A5#": 932.33, "B5": 987.77, "C6": 1046.5, "C6#": 1108.7, "D6": 1174.7, "D6#": 1244.5, "E6": 1318.5, "F6": 1396.9, "F6#": 1480.0, "G6": 1568.0, "G6#": 1661.2, 
                    "A6": 1760.0, "A6#": 1864.7, "B6": 1975.5, "C7": 2093.0, "C7#": 2217.5, "D7": 2349.3, "D7#": 2489.0, "E7": 2637.0, "F7": 2793.0, "F7#": 2960.0, "G7": 3136.0, "G7#": 3322.4,
                    "A7": 3520.0, "A7#": 3729.3, "B7": 3951.1, "C8": 4186.0}
                                                                                                                                    
    notePeriods =     {"A0": 36.36, "A1": 18.18, "A2": 9.091, "A3": 4.545, "A4": 2.273, "A5": 1.136, "A6": .5682, "A7": .2841,
                    "A0#": 34.32, "A1#": 17.16, "A2#": 8.581, "A3#": 4.290, "A4#": 2.145, "A5#": 1.073, "A6#": .5363, "A7#": .2681,
                    "B0": 32.40, "B1": 16.20, "B2": 8.099, "B3": 2.050, "B4": 2.025, "B5": 1.012, "B6": .5062, "B7": .2531,
                    "C1": 30.58, "C2": 15.29, "C3": 7.645, "C4": 3.822, "C5": 1.910, "C6": .9556, "C7": .4778, "C8": .2389,
                    "C1#": 28.86, "C2#": 14.29, "C3#": 7.216, "C4#": 3.608, "C5#": 1.804, "C6#": .9020, "C7#": .4510,
                    "D1": 27.24, "D2": 13.62, "D3": 6.811, "D4": 3.405, "D5": 1.703, "D6": .8513, "D7": .4257,
                    "D1#": 25.71, "D2#": 12.86, "D3#": 6.428, "D4#": 3.214, "D5#": 1.607, "D6#": .8034, "D7#": .4018,
                    "E1": 24.27, "E2": 12.13, "E3": 6.068, "E4": 3.034, "E5": 1.517, "E6": .7584, "E7": .3792,
                    "F1": 22.91, "F2": 11.45, "F3": 5.727, "F4": 2.863, "F5": 1.432, "F6": .7159, "F7": .3580,
                    "F1#": 21.62, "F2#": 10.81, "F3#": 5.405, "F4#": 2.703, "F5#": 1.351, "F6#": .6757, "F7#": .3378,
                    "G1": 20.41, "G2": 10.20, "G3": 5.102, "G4": 2.551, "G5": 1.276, "G6": .6378, "G7": .3189,
                    "G1#": 19.26, "G2#": 9.631, "G3#": 4.816, "G4#": 2.408, "G5#": 1.204, "G6#": .6020, "G7#": .3010}

    notes = []

    for freq in frequency:
        minNote = 5000
        maxNote = 0
        for note in noteFrequencies:
            if freq >= noteFrequencies[note]:
                minNoteFrequency = noteFrequencies[note]
                minNoteNote = note
            else:
                maxNoteFrequency = noteFrequencies[note]
                maxNoteNote = note
                if abs(freq - minNote) > abs(freq - maxNote): notes.append(maxNoteNote)
                elif abs(freq - minNote) < abs(freq - maxNote): notes.append(minNoteNote)
                elif abs(freq - minNote) == abs(freq - maxNote): notes.append(minNoteNote)
                break

    # print(notes)
    # print("\n\n\n")
    # print(len(notes), len(frequency))
    # print(frequency[10], notes[10], "\n", \
    #       frequency[105], notes[105], "\n", \
    #       frequency[541], notes[541], "\n")

    df = pandas.read_csv(fileName.rsplit('.', 1)[0] + '.f0.csv')

print(df["frequency"])




# noteFrequencies = {"A0": 27.500, "A1": 55.000, "A2": 110.00, "A3": 220.00, "A4": 440.00, "A5": 880.00, "A6": 1760.0, "A7": 3520.0,
#                    "A0#": 29.135, "A1#": 58.270, "A2#": 116.54, "A3#": 233.08, "A4#": 466.16, "A5#": 932.33, "A6#": 1864.7, "A7#": 3729.3,
#                    "B0": 30.868, "B1": 61.735, "B2": 123.47, "B3": 246.94, "B4": 493.88, "B5": 987.77, "B6": 1975.5, "B7": 3951.1,
#                    "C1": 32.703, "C2": 65.486, "C3": 130.81, "C4": 161.63, "C5": 523.25, "C6": 1046.5, "C7": 2093.0, "C8": 4186.0,
#                    "C1#": 34.648, "C2#": 69.296, "C3#": 138.59, "C4#": 277.18, "C5#": 554.37, "C6#": 1108.7, "C7#": 2217.5,
#                    "D1": 36.708, "D2": 73.416, "D3": 146.83, "D4": 293.67, "D5": 587.33, "D6": 1174.7, "D7": 2349.3,
#                    "D1#": 38.891, "D2#": 77.782, "D3#": 155.56, "D4#": 311.13, "D5#": 622.25, "D6#": 1244.5, "D7#": 2489.0,
#                    "E1": 41.203, "E2": 82.407, "E3": 164.81, "E4": 329.63, "E5": 659.26, "E6": 1318.5, "E7": 2637.0,
#                    "F1": 43.654, "F2": 87.307, "F3": 174.61, "F4": 349.23, "F5": 698.46, "F6": 1396.9, "F7": 2793.0,
#                    "F1#": 46.249, "F2#": 92.499, "F3#": 185.00, "F4#": 369.99, "F5#": 739.99, "F6#": 1480.0, "F7#": 2960.0,
#                    "G1": 48.999, "G2": 97.999, "G3": 196.00, "G4": 392.00, "G5": 783.99, "G6": 1568.0, "G7": 3136.0,
#                    "G1#": 51.913, "G2#": 103.83, "G3#": 207.65, "G4#": 415.30, "G5#": 830.61, "G6#": 1661.2, "G7#": 3322.4}
