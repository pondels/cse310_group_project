import pygame
from pygame import mixer

mixer.init()

# Currently it only likes .wav extensions so I may change all the files to that

# Path to the audio
filename = ''
mixer.music.load(filename)

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