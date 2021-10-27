import pygame
from pygame import mixer
import time

mixer.init()

# Currently it only likes .wav extensions so I may change all the files to that

# Path to the audio
filename = 'src\wav\coconut.wav'
mixer.music.load(filename)

mixer.music.set_volume(1)

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

mixer.music.play()

while True:
    query = input('')
    if query == 'e':
        mixer.music.stop()
        break