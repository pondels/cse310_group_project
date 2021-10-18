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