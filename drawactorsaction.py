import random

class DisplayActorsAction():

    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720

        # Define Pygame Window
        pass

    def _random_coordinate(self):
        '''
            Grabs 2 points on the window where the line
            of trajectory will start and where the line will end
        '''
        fourPlanes = ['Left', 'Right', 'Top', 'Bottom']
        coordinates = []

        for _ in range(2):
            side = random.choice(fourPlanes)
            fourPlanes.pop(fourPlanes.index(side))
            if side == 'Left':
                plot = random.randrange(0, self.HEIGHT - 1)
                coordinates.append((0, plot))
            elif side == 'Right':
                plot = random.randrange(0, self.HEIGHT - 1)
                coordinates.append((self.WIDTH - 1, plot))
            elif side == 'Top':
                plot = random.randrange(0, self.WIDTH- 1)
                coordinates.append((plot, self.HEIGHT - 1))
            elif side == 'Bottom':
                plot = random.randrange(0, self.WIDTH - 1)
                coordinates.append((plot, 0))
        return coordinates

    def move_line(self, time, start, end, note):
        '''
            Moves the line over a period of time from
            point a (start) to point b (end)

            This "time" variable is dependant on the 
        '''
        pass

display = DisplayActorsAction()
display._random_coordinate()