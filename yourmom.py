import aubio

aubio.slice_source_at_stamps('coconut.wav', [44100], [44100 * 2 - 1])
# print(aubio.slice_source_at_stamps("coconut.wav", timestamps=[15]))