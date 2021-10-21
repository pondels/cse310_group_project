# https://notebook.community/Cortexelus/librosa/examples/LibROSA%20audio%20effects%20and%20playback
# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

# This takes in a youtube URL and downloads it to the system.
# Might get database involved once we get things situated

# import aubio // Rip Aubio :<
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

youtubeLink = input("Please input a valid youtube URL: ")

with ydl:
    result = ydl.extract_info (youtubeLink, download=True)

if 'entries' in result:
    # playlist
    video = result['entires'][0]
else:
    video = result

print(video)
video_url = video['url']
print(video_url)

