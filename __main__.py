import pygame

from src.menu import Menu
from src.drawactorsaction import DrawActorsAction
from src.constants import *

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen) # Comment out if testing
    wav_file, csv_file = menu.menu() # Comment out if testing
    # wav_file = 'DVRSTCLOSEEYES.wav' # Uncomment if testing, put path to wav here
    # csv_file = 'DVRSTCLOSEEYES.f0.csv' # Uncomment if testing, put path to csv here
    display = DrawActorsAction(wav_file)
    display.updateNotes(csv_file)
    display.updateScreen()
    

if __name__ == "__main__":
    main()