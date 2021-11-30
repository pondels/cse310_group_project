# https://notebook.community/Cortexelus/librosa/examples/LibROSA%20audio%20effects%20and%20playback
# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

import os
import glob

from src.youtubeName import videoName

# Takes in the youtube link and converts the file to a .wav format into the directory
class DownloadVideo():

    def __init__(self):
        # I found that using the terminal command for a wav file is much faster than the youtube-dl import for python
        self.file = None
        self.videoName = videoName()

    def download(self, url):
        self.url = url # input("Please enter a valid Youtube URL: ")
        os.system(f"youtube-dl -f bestaudio --extract-audio --audio-format wav --audio-quality 0 {self.url}")

    def renameFile(self):
        data = self.videoName.scrape_info(self.url)
        data = self.videoName.removeCrap(data)
        # Finds all wav files and renames them
        for filename in glob.glob('*.wav'):
            print(filename)
            os.rename(filename, data + ".wav")
            self.file = data + ".wav"

    def deleteFiles(self):
        # DELETES THE CSV AND AUDIO FILE
        for filename in glob.glob('*.wav'):
            os.remove(filename)
        for filename in glob.glob('*.csv'):
            os.remove(filename)
        # If the audio file is for some reason anything else
        for filename in glob.glob('*.m4a'):
            os.remove(filename)
        for filename in glob.glob('*.mp4'):
            os.remove(filename)
        for filename in glob.glob('*.mp3'):
            os.remove(filename)