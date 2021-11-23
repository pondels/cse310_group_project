import glob
import os

class wavToCsv:

    def convertAudio(self):
        for filename in glob.glob('*.wav'):
            os.system(f'crepe {filename}')

        for filename in glob.glob('*.csv'):
            return filename
        