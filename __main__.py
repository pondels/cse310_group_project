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
    # wav_file, csv_file, url = menu.menu() # Comment out if testing
    wav_file = 'BouncingSeals.wav' # Uncomment if testing, put path to wav here
    csv_file = 'BouncingSeals.f0.csv' # Uncomment if testing, put path to csv here
    display = DrawActorsAction(wav_file)
    display.updateNotes(csv_file)
    display.updateScreen()

if __name__ == "__main__":
    main()