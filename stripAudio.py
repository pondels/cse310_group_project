# Source: https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd

import moviepy.editor as mp

def stripAudio(filename):

    my_clip = mp.VideoFileClip(filename)

    my_clip

    my_clip.audio.write_audiofile(r"strip.wav")

stripAudio(f"ZPqZyIKtW0Y.mp4")