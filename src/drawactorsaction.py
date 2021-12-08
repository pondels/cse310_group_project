import pygame
import math
import librosa
import time
import numpy as np
from src.color import Color
from src.constants import *
from pygame import mixer
import librosa.display
import aubio
import time

"""
TODO
Class: DrawActorsAction
Description: What does it do? What does it output? What does it use?
"""

mixer.init()
class DrawActorsAction():

    def __init__(self, filename):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.color = Color()
        self.notes = []

        # Initializes an FPS counter for the Audio to be played at a consistent rate
        self.clock = pygame.time.Clock()
        
        mixer.music.load(filename)
        mixer.music.set_volume(1)

        # Define Pygame Window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Flip Draws the window
        pygame.display.flip()

    """
    TODO
    Class: Color
    Description: What does it do? What does it output? What does it use?
    """
    def updateNotes(self, pitches):
        '''
            A function to add notes to the self.notes
            dictionary.
        '''
        for pitch in pitches:
            if pitch == 0:
                pitch = 20    
            # Grabs the note and the note color from the color class
            # using the freq2color to get an array of the note and its color
            colorArr = self.color.freq2color(pitch)
            noteName = colorArr[0]
            noteColor = colorArr[1]
            # Appends the note, the color, the time, the frequency, and the confidence to the notes array
            self.notes.append([noteName, noteColor, pitch])

    def endpoint(self, angle, line_length):
        Y_additive = math.cos(math.radians(angle)) * line_length
        X_additive = math.sin(math.radians(angle)) * line_length
        return [int((self.WIDTH/2 + X_additive)), int((self.HEIGHT/2 + Y_additive))]

    def updateScreen(self, filename):
            
        background_color = (0, 0, 0)
        self.screen.fill(background_color)

        angle = 0
        
        root = [] 
        count = 0
        for note in self.notes:
            line_length = abs(500 - (note[2] * 3))

            startpoint = [int(self.WIDTH/2), int(self.HEIGHT/2)]
            endpoint = self.endpoint(angle, line_length)

            # checks and updates the angle
            if angle > 0:
                angle -= 1
            else:
                angle = 359
            root.append([note[1], (startpoint, endpoint), angle, (startpoint, endpoint)])
                
        trail_list = []
        trail = 65

        for i in range(trail):
            trail_list.append(root[i])
        count = 0

        first = True

        starting_time = time.time()
        time_stamp = 0

        length = librosa.get_duration(filename=filename)

        ts_interval = length / len(self.notes) # Time Interval

        while self.running:
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # self.clock.tick(90)
            if (time.time() - starting_time) > time_stamp: # Used to control framerate

                if count >= trail: # Adds to the back and pops the front like a queue
                    trail_list.pop(0)
                    trail_list.append(root[count])

                # if count % 20 == True:
                if len(trail_list) == trail: # All items in the trail_list are here
                    divisor = 5 # Base divisor
                    for i in range(20):
                        color = trail_list[i][0]
                        startpoint = trail_list[i][3][0]
                        endpoint = trail_list[i][3][1]
                        angle = trail_list[i][2]

                        Y = math.cos(math.radians(angle))
                        X = math.sin(math.radians(angle))

                        endpoint = [int(endpoint[0]- (X*2)), int(endpoint[1]-(Y*2))]

                        # Quadrants with mATH to make lines "fade"
                        # if 0 <= angle < 90:
                        #     end1 = endpoint[0] + (endpoint[0] / divisor)
                        #     end2 = endpoint[1] + (endpoint[1] / divisor)
                        # elif 90 <= angle < 180:
                        #     end1 = endpoint[0] + (endpoint[0] / divisor)
                        #     end2 = endpoint[1] - (endpoint[1] / divisor)
                        # elif 180 <= angle < 270:
                        #     end1 = endpoint[0] - (endpoint[0] / divisor)
                        #     end2 = endpoint[1] - (endpoint[1] / divisor)
                        # else:
                        #     end1 = endpoint[0] - (endpoint[0] / divisor)
                        #     end2 = endpoint[1] + (endpoint[1] / divisor)

                        # Updates the list with the new information
                        trail_list[i] = [color, [startpoint, endpoint], angle, [startpoint, endpoint]]
                        divisor += 5 # Increases the devisor

                if count < trail:
                    pygame.draw.lines(self.screen, trail_list[count][0], True, trail_list[count][1], 3)
                else:
                    self.screen.fill(background_color)
                    for i in range(trail):
                        pygame.draw.lines(self.screen, trail_list[i][0], True, trail_list[i][1], 3)

                if first:
                    mixer.music.play()
                    first = False

                pygame.display.flip()

                time_stamp += ts_interval # IF NOT WORKING, SET TO .01
                count += 1

                if count == len(root):
                    self.running = False

