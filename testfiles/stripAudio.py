# Source: https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd

import moviepy.editor as mp


"""
TODO
function: stripAudio
Input: the name of a video file (e.g. mp4)
Output: nothing
Description: Takes the name of the video file, stores the video file, and saves
the video file to a wav file called strip.wav in the root directory of the
program project
"""
def stripAudio(filename):
    # grabs a video clip for a file path
    my_clip = mp.VideoFileClip(filename)

    # Writes it to an audio file
    my_clip.audio.write_audiofile(r"strip.wav")

# Test it out with this file
stripAudio(f"Charlie bit my finger again.mp4")

# I found while looking at audio realtime that this can 'split' the audio into 2 tracks.
# The main part of the music and the beat of the music, or mainly just the bass.
# y, sr = librosa.load('src\wav\coconut.wav')
# y_harm, y_perc = librosa.effects.hpss(y)

# ^^^ This is the code, but Refer to @showGraph.py in testfiles to see how it works and what it shows