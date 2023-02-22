from Dot import * 

class ListDot:
    # ============================== CONSTRUCTOR OF LIST ==============================
    def __init__(self, dimension, neff):
        # Initiate the number of dots, dimension of dot and the list of dots
        self.neff = neff
        self.dimension = dimension
        self.buffer = []
        self.euclid_count = 0

    def generateRandom(self):
        # Fill the buffer with randomly generated dots and sort it by the x-coordinate
        self.buffer = [Dot(self.dimension) for i in range (self.neff)]
        self.buffer.sort(key = lambda x: x.position[0])

    # ================================== BRUTE FORCE ==================================
    def bruteForce(self, start, finish):
        # Initialize the value 
        minDist = 999999
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
        if (finish-start+1 <= 4):
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
            # TO DO for Austin

            # Compare the minDist between pair of dots across the midline and pair of dots from the same partition
            # TO DO for Austin

        return dot1, dot2, minDist
    
    # =============================== HELPER SECTION =================================
    def printAllDots(self):
        # Print the information of all dots. For debugging
        for i in range(self.neff):
            self.buffer[i].printDot()
            print()

    def plotFor3D(self, dot1, dot2):
        # Visualize the closest pair
        # TO DO for Austin
        pass



## =============================== TEMP TESTING =================================
## Source code to test between brute force and divide and conquer

# # Change the 100 to number of dots
# t1 = ListDot(3, 100)         
# t1.generateRandom()

# # Optional
# t1.printAllDots()

# # Calculation
# dot1, dot2, minDist = t1.divideAndConquer(0, t1.neff - 1)
# dot3, dot4, minDist2 = t1.bruteForce(0, t1.neff-1)
# print("\nDivide and conquer result: ")
# dot1.printDot()
# dot2.printDot()
# print(f"\nMinimal distance:{minDist}\n")
# print("Bruteforce result: ")
# dot3.printDot()
# dot4.printDot()
# print(f"\nMinimal distance:{minDist2}")