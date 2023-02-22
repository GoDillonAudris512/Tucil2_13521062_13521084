# File          : Dot.py
# Description   : Implement the dot object and its method

import random
import math

class Dot:
    def __init__(self, dimension):
        # Initiate the number of dimension of dot and its position
        self.dimension = dimension
        self.position = [random.randint(-1000, 1000) for i in range (dimension)]
    
    def __sub__(self, other):
        # EUCLIDEAN DISTANCE FUNCTION
        # Calculate the distance between this dot and other dot
        distance_squared = 0
        
        for i in range(0, self.dimension):
            distance_squared += math.pow((other.position[i]-self.position[i]), 2)

        return math.sqrt(distance_squared)
    
    def printDot(self):
        # Print the position of this dot
        print(f"[{self.position[0]}", end="")
        for i in range(1, self.dimension):
            print(f", {self.position[i]}", end="")
        print("]")