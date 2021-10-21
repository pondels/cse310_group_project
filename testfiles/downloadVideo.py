# https://notebook.community/Cortexelus/librosa/examples/LibROSA%20audio%20effects%20and%20playback
# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

# This takes in a youtube URL and downloads it to the system.
# Might get database involved once we get things situated

# import aubio // Rip Aubio :<

from youtubeName import videoName
import os

videoname = videoName()

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

youtubeLink = input("Please input a valid youtube URL: ")
realName = videoname.scrape_info(youtubeLink)

with ydl:
    result = ydl.extract_info (youtubeLink, download=True, )

if 'entries' in result:
    # playlist
    video = result['entires'][0]
else:
    video = result

# print(video)
video_id = video['id']
print(video_id)
# https://youtu.be/bXkRj-UcWVM

# This is assuming the file is made using the .mp4 extention
# Try excepts can be made to change the file to a .mp4 if it returns a noFileFound
os.rename(f'{video_id}.mp4', f'{realName}.mp4')

