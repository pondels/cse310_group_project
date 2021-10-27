# https://notebook.community/Cortexelus/librosa/examples/LibROSA%20audio%20effects%20and%20playback
# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

import os

from src.youtubeName import videoName

# Takes in the youtube link and converts the file to a .wav format into the directory
class DownloadVideo():

    def __init__(self):
        # I found that using the terminal command for a wav file is much faster than the youtube-dl import for python
        self.file = None
        self.videoName = videoName()

    def download(self):
        self.url = input("Please enter a valid Youtube URL: ")
        os.system(f"youtube-dl -f bestaudio --extract-audio --audio-format wav --audio-quality 0 {self.url}")

    def renameFile(self):
        data = self.videoName.scrape_info(self.url)
        data = self.videoName.removeCrap(data)
        print(data)

    def retrieve_audio(self):
        pass

    def retrieve_csv(self):
        print("You get the csv file path")
# Link for testing https://youtu.be/bXkRj-UcWVM