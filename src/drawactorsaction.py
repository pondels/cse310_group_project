import random
import pygame
import asyncio
import time
import math
from src.mathEQ import Math
from src.color import Color
from src.constants import *

"""
TODO
Class: DisplayActorsAction
Description: What does it do? What does it output? What does it use?
"""

from pygame import mixer

mixer.init()

class DisplayActorsAction():

    def __init__(self, filename):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.math = Math()
        self.color = Color()
        self.notes = []

        # Initializes an FPS counter for the Audio to be played at a consistent rate
        self.clock = pygame.time.Clock()
        
        mixer.music.load(filename)
        mixer.music.set_volume(1)

        # Define Pygame Window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # TODO Why are we flipping the display?
        pygame.display.flip()

    """
    TODO
    Class: Color
    Description: What does it do? What does it output? What does it use?
    """
    def updateNotes(self, csvFile):
        '''
            A function to add notes to the self.notes
            dictionary.
        '''
        # Opens the CSV File to Read
        print(PATH)
        with open(f"{PATH}\{csvFile}", "r") as file:
            # Skips the first line in the file
            next(file)

            # Iterates through each line in the CSV File
            for i in file:
                # Splits each line up into an array
                # using the Time, Frequency, and Confidence
                new_i = i.strip("\n")
                new_i = new_i.split(',')
                print(new_i)
                if new_i != ['']:
                    if new_i[1] == '0.0':
                        new_i.pop(1)
                        new_i.insert(1, 0.1)
                    print(new_i)
                    time = float(new_i[0])
                    frequency = float(new_i[1])
                    confidence = float(new_i[2])
                    # Grabs the note and the note color from the color class
                    # using the freq2color to get an array of the note and its color
                    colorArr = self.color.freq2color(frequency)
                    noteName = colorArr[0]
                    noteColor = colorArr[1]
                    # Appends the note, the color, the time, the frequency, and the confidence to the notes array
                    self.notes.append([noteName, noteColor, time, frequency, confidence])


    def updateSpiral(self, time, start, end, note):
        '''
            Moves the line over a period of time from
            point a (start) to point b (end)

            This "time" variable is dependant on the 
        '''
        # Is this ^ The description of the function?
        pass

    def updateScreen(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            background_color = (0, 0, 0)
            self.screen.fill(background_color)

            line_length = 20
            angle = 90
            
            mixer.music.play()

            for note in self.notes:

                self.clock.tick(100)

                mid_X = self.WIDTH/2
                mid_Y = self.HEIGHT/2
                XQ = 1
                YQ = 1
                startpoint = [int(mid_X), int(mid_Y)]
                Y_additive = math.cos(math.radians(angle)) * line_length
                X_additive = math.sin(math.radians(angle)) * line_length
                if angle < 0 and angle > -90:
                    XQ = -1
                    YQ = 1
                if angle < -90 and angle > -180:
                    XQ = -1
                    YQ = -1
                if angle < -180 and angle > -270:
                    XQ = 1
                    YQ = -1
                else:
                    XQ= 1
                    YQ = 1
                endpoint = [int((mid_X + X_additive) * XQ), int((mid_Y + Y_additive)*YQ)]
                

                time.sleep(.01)
                pygame.draw.lines(self.screen, note[1], True, (startpoint, endpoint), 3)
                pygame.display.flip()
                angle = angle - 1
                line_length+=.5
                if angle == -270:
                    angle = 90
            self.running = False