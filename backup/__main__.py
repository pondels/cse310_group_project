from src.constants import *


from src.drawactorsaction import DrawActorsAction
from src.downloadVideo import DownloadVideo

def main():
    
    '''
    PLEASE USE https://youtu.be/bXkRj-UcWVM AS A TEST FILE.
    ITS JUST A SHORT AUDIO FILE THAT CAN BE USED WHILE TESTING
    MAIN.
    '''


    # download_video = DownloadVideo()
    # # Downloads a File Using a Valid Youtube URL
    # download_video.download()
    # # Finds the .wav and .csv file that was just downloaded
    # # And Returns the path for both files.
    # audioFile = download_video.retrieve_audio()
    # csvFile = download_video.retrieve_csv()
    # download_video.renameFile()

    # Currently Temporary inputs for audio and csv
    # While I work on getting pathing figured out
    audioFile = 'src\wav\Ladies & Gentlemen.... We Got Him _ ORIGINAL MEME HD--15VC4Yxzys.wav'
    # use csv as the starting file and NOT src\
    csvFile = 'csv\Ladies & Gentlemen.... We Got Him _ ORIGINAL MEME HD--15VC4Yxzys.wav.csv'
    # Display takes in the audioFile
    display = DrawActorsAction(audioFile)
    # display._random_coordinate()

    # UpdateNotes takes in the csvFile
    display.updateNotes(csvFile)
    # Starts drawing the cube with the csv file
    display.updateScreen()

if __name__ == "__main__":
    main()