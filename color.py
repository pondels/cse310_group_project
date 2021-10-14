
# TODO Quick explanation of librosa and what we're doing with it
import librosa as librosa
"""
Class: Color
Description: Color class holds a dictionary of all the notes and their corresponding rgb value.
"""
class Color():

    def __init__(self):
        self.colors = {
            # ORANGE
            "A":(255, 136, 0),
            # YELLOW
            "A♯":(238, 255, 1),
            # LIME
            "B":(154, 244, 0),
            # GREEN
            "C":(0, 231, 1),
            # CYAN
            "C♯":(0, 254, 174),
            # OCEAN
            "D":(0, 108, 255),
            # BLUE
            "D♯":(47, 0, 245),
            # VIOLET
            "E":(129, 0, 206),
            # PURPLE
            "F":(64, 0, 87),
            # MAROON
            "F♯":(102, 4, 81),
            # RED
            "G":(216, 0, 0),
            # RED-ORANGE
            "G♯":(226, 67, 1)
        }

    """
    Function: freq2color
    Description: freq2color takes in a frequency and outputs a list with the note name and color.
    """
    def freq2color(self, freq):
        noteName = librosa.hz_to_note(freq)
        
        noteColor = self.colors.get(noteName[:-1])

        note = [noteName, noteColor]
        return note

color = Color()
newColor = color.freq2color(695)
print(newColor)
