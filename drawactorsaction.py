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

        # Define Pygame Window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.flip()

    def _random_coordinate(self):
        '''
            Grabs 2 points on the window where the line
            of trajectory will start and where the line will end
        '''
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

    def move_line(self, time, start, end, note):
        '''
            Moves the line over a period of time from
            point a (start) to point b (end)

            This "time" variable is dependant on the 
        '''
        pass

    def updateScreen(self, thickness):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)
            slope = self.math.slope(self.coordinates[0][0], self.coordinates[0][1], self.coordinates[1][0], self.coordinates[1][1])
            notes = [i for i in range(100, 1300)]
            print((self.coordinates[0], self.coordinates[1]))
            print((self.coordinates[0][0]-1, self.coordinates[0][1]-1), (self.coordinates[1][0]-1, self.coordinates[1][1]-1))
            colorSpec = self.colour.note2colour(random.choice(notes))
            for i in range(thickness):
                pygame.draw.aalines(self.screen, colorSpec, True, ((self.coordinates[0][0]-i, self.coordinates[0][1]-i), (self.coordinates[1][0]-i, self.coordinates[1][1]-i)))
            pygame.display.flip()
            time.sleep(1)
            self._random_coordinate()

display = DisplayActorsAction()
display._random_coordinate()
display.updateScreen(random.randrange(45))