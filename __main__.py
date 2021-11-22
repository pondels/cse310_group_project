import pygame

from src.menu import Menu
from src.drawactorsaction import DrawActorsAction
from src.constants import *

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen)
    wav_file = menu.menu()
    csv_file = "csv\coconut.f0.csv"
    display = DrawActorsAction(wav_file)
    display.updateNotes(csv_file)
    display.updateScreen()
    

if __name__ == "__main__":
    main()