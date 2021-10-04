# https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd

import moviepy.editor as mp

my_clip = mp.VideoFileClip(f"ZPqZyIKtW0Y.mp4")

my_clip

#This is still unfinished. Still need to add the function to get the audio out

my_clip.audio.write_audiofile(r"my_result.wav")