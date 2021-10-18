
# This will generate a random point on the edge of the screen.

# Designed for 1280×720 resolution

import random

def randEdge():
    # Picks a random side of the screen
    side = random.randrange(3)

    # Returns a random point along the randomly picked side
    return {
        0: (0,random.randrange(720)),
        1: (1280,random.randrange(720)),
        2: (random.randrange(1280),0),
        3: (random.randrange(1280),720)
    }[side]

# Returns the coordinate for testing purposes
print(randEdge())


