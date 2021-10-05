import librosa as librosa

class Colour():

    def __init__(self):
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

    def note2colour(self, freq):
        noteName = librosa.hz_to_note(freq)
        
        noteColour = self.colours.get(noteName[:-1])
        print(noteColour)
        return noteColour

# colour = Colour()
# colour.note2colour(695)
