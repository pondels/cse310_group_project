import random
import pygame
import time
from mathEQ import Math
from colour import Colour

"""
TODO
Class: DisplayActorsAction
Description: What does it do? What does it output? What does it use?
"""

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
        # TODO What's this | ?
        #                  V
        self.notes = [{"id": 0, "color": (random.randrange(255), random.randrange(255), random.randrange(255)), "time":4.1459999, "thickness": random.randrange(65)}]

        # Define Pygame Window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # TODO Why are we flipping the display?
        pygame.display.flip()

    """
    TODO
    Function: _random_coordinate
    Description: What does it do? What does it output? What does it use?
    """
    def _random_coordinate(self):
        '''
            Grabs 2 points on the window where the line
            of trajectory will start and where the line will end
        '''
        # Is this ^ The description of the function?

        fourPlanes = ['Left', 'Right', 'Top', 'Bottom']
        self.coordinates = []

        for _ in range(2):
            side = random.choice(fourPlanes)
            fourPlanes.pop(fourPlanes.index(side))
            if side == 'Left':
                plot = random.randrange(0, self.HEIGHT - 1)
                self.coordinates.append((0, plot))
            elif side == 'Right':
                plot = random.randrange(0, self.HEIGHT - 1)
                self.coordinates.append((self.WIDTH - 1, plot))
            elif side == 'Top':
                plot = random.randrange(0, self.WIDTH- 1)
                self.coordinates.append((plot, self.HEIGHT - 1))
            elif side == 'Bottom':
                plot = random.randrange(0, self.WIDTH - 1)
                self.coordinates.append((plot, 0))
        return self.coordinates

    """
    TODO
    Class: Colour
    Description: What does it do? What does it output? What does it use?
    """
    def updateNotes(self):
        '''
            A function to add and pop notes
            based on time we want them to be on screen.
        '''
        # Is this ^ The description of the function?
        pass

    def move_line(self, time, start, end, note):
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
            
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)

            # SLOPE GOING TO BE USED FOR DRAWING THE LINE SLOWLY ACROSS THE SCREEN
            slope = self.math.slope(self.coordinates[0][0], self.coordinates[0][1], self.coordinates[1][0], self.coordinates[1][1])
            
            # notes = [i for i in range(100, 1300)]
            # colorSpec = self.colour.note2colour(random.choice(notes))
            for note in range(len(self.notes)):
                for i in range(self.notes[note]["thickness"]):
                    pygame.draw.aalines(self.screen, self.notes[note]['color'], True, ((self.coordinates[0][0]-i, self.coordinates[0][1]-i), (self.coordinates[1][0]-i, self.coordinates[1][1]-i)))
            pygame.display.flip()
            time.sleep(1)
            self._random_coordinate()

display = DisplayActorsAction()
display._random_coordinate()
display.updateScreen()