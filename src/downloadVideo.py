# https://notebook.community/Cortexelus/librosa/examples/LibROSA%20audio%20effects%20and%20playback
# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

import os

# Takes in the youtube link and converts the file to a .wav format into the directory

# I found that using the terminal command for a wav file is much faster than the youtube-dl import for python
url = input("Please enter a valid Youtube URL: ")
os.system(f"youtube-dl -f bestaudio --extract-audio --audio-format wav --audio-quality 0 {url}")

# Link for testing https://youtu.be/bXkRj-UcWVM