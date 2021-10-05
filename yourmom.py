import aubio
import essentia
# import youtube_dl

# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

# with ydl:
#     result = ydl.extract_info ("https://www.youtube.com/watch?v=ZPqZyIKtW0Y", download=True)

# if 'entries' in result:
#     # playlist
#     video = result['entires'][0]
# else:
#     video = result

# print(video)
# video_url = video['url']
# print(video_url)

aubio.slice_source_at_stamps('coconut.wav', [44100], [44100 * 5 - 1])
# print(aubio.slice_source_at_stamps("coconut.wav", timestamps=[15]))

aubio.freq2note()