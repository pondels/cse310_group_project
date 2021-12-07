import pygame
pygame.init()
# import webbrowser
from src.menu import Menu
from src.drawactorsaction import DrawActorsAction
from src.constants import *

# Link for testing https://youtu.be/-SjPVVeNdKY
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen) # Comment out if testing
    # URL MIGHT BE USED FOR SHOWING A VIDEO, USELESS FOR NOW
    wav_file, csv_file, url = menu.menu() # Comment out if testing
    # wav_file = 'TuvanThroatSinging.wav' # Uncomment if testing, put path to wav here
    # csv_file = 'TuvanThroatSinging.f0.csv' # Uncomment if testing, put path to csv here
    display = DrawActorsAction(wav_file)
    display.updateNotes(csv_file)
    display.updateScreen()

    # 1) https://youtu.be/qx8hrhBZJ98  3:52 Ratio: +6
    # 2) https://youtu.be/pTA0DSfrGZ0  4:15 Ratio: +
    # 3) https://youtu.be/3Z1h2VE0hzs  1:47 Ratio: +2.8
    # 4) https://youtu.be/V0e7rFdVYxE 10:41 Ratio: +
    # 5) https://youtu.be/Wl9oUBgFk6Y  0:43 Ratio: +2

if __name__ == "__main__":
    main()