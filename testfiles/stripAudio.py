# Source: https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd

from __future__ import print_function
import moviepy.editor as mp
import librosa
import librosa.display
import IPython.display
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt



"""
function: stripAudio
Input: the name of an audio file (e.g. wav)
Output: nothing
Description: Takes the name of the audio file, stores the audio file, and saves
the video file to a wav file called strip.wav in the root directory of the
program project
"""
def stripAudio():
    y, sr = librosa.load('src/wav/coconut.wav')

    # ONLY UNCOMMENT OUT ONE IPYTHON.DISPLAY AT A TIME.
    # ONLY THE LAST ONE WILL BE RECOGNIZED OTHERWISE

    # This just plays the normal music
    sf.write('src/wav/normal.wav', y, sr)

    # UNCOMMENT THE Y_H, Y_P WITH ONE OF THE IPYTHON.DISPLAYS
    # COMMENT IT OUT IF JUST LOADING THE TOP AUDIO
    y_h, y_p = librosa.effects.hpss(y)

    # This play the horizontal audio, aka, very flat music.
    sf.write('src/wav/flat.wav', y_h, sr)

    # This Plays mainly the percussive Audio. Aka, the beat
    sf.write('src/wav/beat.wav', y_p, sr)
    




"""
function: stripAudioVideo
Input: the name of a video file (e.g. mp4)
Output: nothing
Description: Takes the name of the video file, stores the video file, and saves
the video file to a wav file called strip.wav in the root directory of the
program project
"""
def stripAudioVideo(filename):
    # grabs a video clip for a file path
    my_clip = mp.VideoFileClip(filename)

    # Writes it to an audio file
    my_clip.audio.write_audiofile(r"strip.wav")



# Test it out with this file
# stripAudioVideo(f"Charlie bit my finger again.mp4")

stripAudio()

# I found while looking at audio realtime that this can 'split' the audio into 2 tracks.
# The main part of the music and the beat of the music, or mainly just the bass.
# y, sr = librosa.load('src\wav\coconut.wav')
# y_harm, y_perc = librosa.effects.hpss(y)

# ^^^ This is the code, but Refer to @showGraph.py in testfiles to see how it works and what it shows