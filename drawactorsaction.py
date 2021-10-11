import random
import pygame
import time
from mathEQ import Math
from colour import Colour

class DisplayActorsAction():

    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.math = Math()
        self.colour = Colour()

        # [{"id": 0, "color": (125, 41, 0), "time": 4.145999...},
        #  {''},
        #  {''}] How we structure the notes
        self.notes = []

        # Define Pygame Window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.flip()

    def updateNotes(self):
        '''
            A function to add notes to the self.notes
            dictionary.
        '''

        pass

    def move_line(self, time, start, end, note):
        '''
            Moves the line over a period of time from
            point a (start) to point b (end)

            This "time" variable is dependant on the 
        '''
        pass

    def updateScreen(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)

            # SLOPE GOING TO BE USED FOR DRAWING THE LINE SLOWLY ACROSS THE SCREEN
            slope = self.math.slope(self.coordinates[0][0], self.coordinates[0][1], self.coordinates[1][0], self.coordinates[1][1])
            
            for note in range(len(self.notes)):
                for i in range(self.notes[note]["thickness"]):
                    pygame.draw.aalines(self.screen, self.notes[note]['color'], True, ((self.coordinates[0][0]-i, self.coordinates[0][1]-i), (self.coordinates[1][0]-i, self.coordinates[1][1]-i)))
            pygame.display.flip()
            time.sleep(.1)
            self._random_coordinate()

display = DisplayActorsAction()
display._random_coordinate()
display.updateScreen()