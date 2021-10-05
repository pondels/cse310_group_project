import random
import pygame
import time
from mathEQ import Math

class DisplayActorsAction():

    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.math = Math()

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

    def updateScreen(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)
            slope = self.math.slope(self.coordinates[0][0], self.coordinates[0][1], self.coordinates[1][0], self.coordinates[1][1])
            print(slope)
            pygame.draw.aalines(self.screen, (random.randrange(255), random.randrange(255), random.randrange(255)), True, (self.coordinates[0], self.coordinates[1]))
            pygame.display.flip()
            time.sleep(.05)
            self._random_coordinate()

display = DisplayActorsAction()
display._random_coordinate()
display.updateScreen()