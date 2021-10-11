
# TODO Quick explanation of librosa and what we're doing with it
import librosa as librosa
"""
TODO
Class: Colour
Description: What does it do? What does it output? What does it use?
"""
class Colour():

    def __init__(self):
        # What are these? TODO
        self.colours = {
            "A":(117,0,0),
            "A♯":(255,236,0),
            "B":(153,255,0),
            "C":(40,255,0),
            "C♯":(0,255,232),
            "D":(0,124,255),
            "D♯":(5,0,255),
            "E":(69,0,234),
            "F":(87,0,158),
            "F♯":(116,0,0),
            "G":(179,0,0),
            "G♯":(238,0,0)
        }
    """
    TODO
    Function: note2colour
    Description: What does it do? What does it output? What does it use?
    """
    def note2colour(self, freq):
        # What do these do? How does it do it? TODO
        noteName = librosa.hz_to_note(freq)
        
        noteColour = self.colours.get(noteName[:-1])

        note = [noteName, noteColour]
        return note

# colour = Colour()
# colour.note2colour(695)
