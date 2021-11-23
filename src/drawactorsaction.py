import random
import pygame
import asyncio
import time
import math
import librosa
import numpy as np
from src.color import Color
from src.constants import *

"""
TODO
Class: DrawActorsAction
Description: What does it do? What does it output? What does it use?
"""

from pygame import mixer

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
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            background_color = (0, 0, 0)
            self.screen.fill(background_color)

            line_length = 40
            angle = 0
            
            mixer.music.play()
            backwards = []
            
            

            for note in self.notes:
                self.clock.tick(100)

                mid_X = self.WIDTH/2
                mid_Y = self.HEIGHT/2

                startpoint = [int(mid_X), int(mid_Y)]
                Y_additive = math.cos(math.radians(angle)) * line_length
                X_additive = math.sin(math.radians(angle)) * line_length

                endpoint = [int((mid_X + X_additive)), int((mid_Y + Y_additive))]
                
                
                pygame.draw.lines(self.screen, note[1], True, (startpoint, endpoint), 3)
                pygame.display.flip()
                # backwards.append([note[1], startpoint, endpoint])
                
                


                # checks and updates the angle
                if angle > 0:
                    angle -= 1
                else:
                    angle = 359

                line_length = (note[3])
                #  + 220) / note[2]
                # line_length = line_length + .5
            # print(backwards) 

            # for i in range(len(backwards)):
            #     zi = len(backwards)-i
            #     print(backwards[zi])
            #     pygame.draw.lines(self.screen, backwards[zi][0], True, (backwards[zi][1], backwards[zi][2]), 3)
            #     pygame.display.flip()

            self.running = False

class AudioAnalyzer:

    def __init__(self):

        self.frequencies_index_ratio = 0  # array for frequencies
        self.time_index_ratio = 0  # array of time periods
        self.spectrogram = None  # a matrix that contains decibel values according to frequency and time indexes

    def load(self, filename):

        time_series, sample_rate = librosa.load(filename)  # getting information from the file

        # getting a matrix which contains amplitude values according to frequency and time indexes
        stft = np.abs(librosa.stft(time_series, hop_length = 512, n_fft = 2048 * 4))

        self.spectrogram = librosa.amplitude_to_db(stft, ref = np.max)  # converting the matrix to decibel matrix

        frequencies = librosa.core.fft_frequencies(n_fft = 2048 * 4)  # getting an array of frequencies

        # getting an array of time periodic
        times = librosa.core.frames_to_time(np.arange(self.spectrogram.shape[1]), sr=sample_rate, hop_length = 512, n_fft = 2048 * 4)

        self.time_index_ratio = len(times)/times[len(times) - 1]

        self.frequencies_index_ratio = len(frequencies) / frequencies[len(frequencies) - 1]
