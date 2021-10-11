import random


# This will generate a random point on the edge of the screen.
# Designed for 1280×720 resolution
def randEdge(self):
    side = random.randrange(3)

    return {
        0: (0,random.randrange(720)),
        1: (1280,random.randrange(720)),
        2: (random.randrange(1280),0),
        3: (random.randrange(1280),720)
    }[side]

class Star():

    def __init__(self):

        startCoords = randEdge()

        pass

    def length(self):
        '''
            Returns the length of the "star"
        '''
        pass

    def time(self):
        '''
            Returns how long the "star" stays on screen for
        '''
        pass

