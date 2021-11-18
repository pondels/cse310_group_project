import pygame

from src.menu import Menu
from src.constants import *

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen)
    menu.menu()
    

if __name__ == "__main__":
    main()