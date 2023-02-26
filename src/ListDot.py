from Dot import * 
import matplotlib.pyplot as plt
import numpy as np
from ListDot import * 

class ListDot:
    # ============================== CONSTRUCTOR OF LIST ==============================
    def __init__(self, dimension, neff):
        # Initiate the number of dots, dimension of dot, list of dots, and number of euclid distance function called
        self.neff = neff
        self.dimension = dimension
        self.euclid_count = 0
        self.buffer = [Dot(self.dimension) for i in range (self.neff)]

        # Sort the array according to x-coordinate with quicksort algorithm
        self.quickSort(0, self.neff-1)

    def quickSort(self, start, finish):
        # Initialize the pointer
        left = start
        right = finish

        # If the array contains more than 1 element, do the quicksort
        if (start < finish):
            i = self.partition(start, finish)
            self.quickSort(start, i-1)
            self.quickSort(i+1, finish)
            
    def partition(self, start, finish):
        # Initialize the pointer and pivot
        left = start
        right = finish
        pivotVal = self.buffer[(start+finish) // 2].position[0]

        # Partition the array into left and right. End of partition, pivot in the correct place
        while (left < right):
            while (self.buffer[left].position[0] < pivotVal):
                left += 1

            while (self.buffer[right].position[0] > pivotVal):
                right -= 1

            self.buffer[left], self.buffer[right] = self.buffer[right], self.buffer[left]
        
        # Undo the last swap
        self.buffer[left], self.buffer[right] = self.buffer[right], self.buffer[left]

        # Return the pivot index
        return right
            
    # ================================== BRUTE FORCE ==================================
    def bruteForce(self, start, finish):
        # Initialize the value 
        minDist = np.inf
        dot1 = Dot(self.dimension)
        dot2 = Dot(self.dimension)
        euclid_count = 0

        # Calculate the closest pair of dots using brutefore
        for i in range (start, finish):
            for j in range(i+1, finish+1):
                euclid_count += 1
                temp = self.buffer[j] - self.buffer[i]
                if (temp < minDist):
                    minDist = temp
                    dot1 = self.buffer[i]
                    dot2 = self.buffer[j]

        # Return the closest pair of dots and their distance
        return dot1, dot2, minDist, euclid_count
    
    # ============================== DIVIDE AND CONQUER ===============================
    def divideAndConquer(self, start, finish):
        # Initialize the value
        minDist = 999999
        dot1 = Dot(self.dimension)
        dot2 = Dot(self.dimension)

        # Process the list depending on its size
        if (finish-start+1 <= 3):
            # Find the closest pair of dots using bruteforce
            dot1, dot2, minDist, count = self.bruteForce(start, finish)
            self.euclid_count += count
        else:
            # Define the size of current partition
            size = finish - start + 1

            # Partition the list of dots into left and right
            dot3, dot4, minDistLeft = self.divideAndConquer(start, start + (size // 2) - 1)
            dot5, dot6, minDistRight = self.divideAndConquer(start + (size // 2), finish)

            # Determine the minimum distance (either from left partition or right partition)
            if (minDistLeft <= minDistRight):
                dot1, dot2, minDist = dot3, dot4, minDistLeft
            else:
                dot1, dot2, minDist = dot5, dot6, minDistRight

            # Calculate the closest pair of dots across the midline with width current minDist
            # Find x point where it is the middle point among all dots
            locX = (finish + start) // 2
            midX = self.buffer[locX].position[0]

            # Make an array of all dots from mindist to left and minDist to right
            p = start
            while abs(self.buffer[p].position[0] - midX) > minDist:
                p += 1
            left = p 
            p += 1
            while  p <= finish and abs(self.buffer[p].position[0] - midX) <= minDist:
                p += 1
            right = p-1

            # Compare the minDist between pair of dots across the midline and pair of dots from the same partition
            for i in range (left, right) :
                for j in range (i+1, right+1) :
                    if (self.buffer[i].checkDimensionDistance(self.buffer[j], minDist)) :
                        jarak = self.buffer[i]-self.buffer[j]
                        self.euclid_count += 1
                        if jarak < minDist : 
                            minDist = jarak
                            dot1, dot2 = self.buffer[i], self.buffer[j]
        return dot1, dot2, minDist
    
    # =============================== HELPER SECTION =================================
    def printAllDots(self):
        # Print the information of all dots. For debugging
        for i in range(self.neff):
            self.buffer[i].printDot()
            print()

    def plotFor3D(self, dot1, dot2):
        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Generate some 3D data
        for i in range(self.neff) :
            if (self.buffer[i] != dot1 and self.buffer[i] != dot2) :
                ax.scatter(self.buffer[i].position[0], self.buffer[i].position[1], self.buffer[i].position[2], c='blue', marker='o')

        # Creating the title
        ax.set_title("Pasangan Titik Terdekat 3D")

        # Plot the nearest dots using scatter plot
        ax.scatter(dot1.position[0], dot1.position[1], dot1.position[2], c='red', marker='x')
        ax.scatter(dot2.position[0], dot2.position[1], dot2.position[2], c='red', marker='x')

        # Set the labels name for the axes
        ax.set_xlabel('Sumbu X')
        ax.set_ylabel('Sumbu Y')
        ax.set_zlabel('Sumbu Z')

        # Show the plot
        plt.show()