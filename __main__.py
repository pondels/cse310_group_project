import pygame
pygame.init()
from src.menu import Menu
from src.drawactorsaction import DrawActorsAction
from src.constants import *

''' TESTING LINKS FOR DEMO

    Pitch Detection (pain): https://www.youtube.com/watch?v=SEy_7dAFlqk&ab_channel=mostannoyingsounds
    Large Audio File: https://www.youtube.com/watch?v=ztzq05IzYds&t=273s&ab_channel=Jacaranda

'''

# Link for testing https://youtu.be/-SjPVVeNdKY
# https://youtu.be/V0e7rFdVYxE

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen)
    wav_file, pitches = menu.menu()

    display = DrawActorsAction(wav_file)
    display.updateNotes(pitches)
    display.updateScreen(wav_file)

if __name__ == "__main__":
    main()