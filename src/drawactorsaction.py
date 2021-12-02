import pygame
import math
import librosa
import numpy as np
from src.color import Color
from src.constants import *
from pygame import mixer

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
    def updateNotes(self, csvFile):
        '''
            A function to add notes to the self.notes
            dictionary.
        '''
        # Opens the CSV File to Read
        with open(csvFile, "r") as file:
            # Skips the first line in the file
            next(file)

            # Iterates through each line in the CSV File
            for i in file:
                # Splits each line up into an array
                # using the Time, Frequency, and Confidence
                new_i = i.strip("\n")
                new_i = new_i.split(',')
                if new_i != [''] and new_i[1] != '0.000':
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
            
        background_color = (0, 0, 0)
        self.screen.fill(background_color)

        angle = 0
        
        root = [] 
        count = 0
        for note in self.notes:
            line_length = abs(500 - note[3])

            mid_X = self.WIDTH/2
            mid_Y = self.HEIGHT/2

            startpoint = [int(mid_X), int(mid_Y)]
            Y_additive = math.cos(math.radians(angle)) * line_length
            X_additive = math.sin(math.radians(angle)) * line_length
            endpoint = [int((mid_X + X_additive)), int((mid_Y + Y_additive))]

            # checks and updates the angle
            if angle > 0:
                angle -= 1
            else:
                angle = 359
            root.append([note[1], (startpoint, endpoint)])
                
        trail_list = []
        trail = 360

        for i in range(trail):
            trail_list.append(root[i])
        count = 0

        first = True

        while self.running:

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clock.tick(100)
            if count >= trail:
                trail_list.pop(0)
                trail_list.append(root[count])
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
            
            count += 1
            if count == len(root):
                self.running = False

