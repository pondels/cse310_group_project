import pygame
pygame.init()
from src.menu import Menu
from src.drawactorsaction import DrawActorsAction
from src.constants import *

# Link for testing https://youtu.be/-SjPVVeNdKY
# https://youtu.be/V0e7rFdVYxE
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen) # Comment out if testing
    wav_file, s, samplerate = menu.menu() # Comment out if testing

    display = DrawActorsAction(wav_file)
    display.updateNotes(s, samplerate)
    display.updateScreen()

if __name__ == "__main__":
    main()