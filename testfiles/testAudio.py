import pygame
from pygame import mixer

mixer.init()

mixer.music.load('src\wav\coconut.wav')

mixer.music.set_volume(1)

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

mixer.music.play()

while True:
    query = input('')
    if query == 'e':
        mixer.music.stop()
        break