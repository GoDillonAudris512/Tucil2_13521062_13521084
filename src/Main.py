# File          : Main.py
# Description   : For interface with user and start the algorithm to find closest pair of dots

import time
from ListDot import *

class Main:
    @staticmethod

    def askForDotNumber():
        # Validate the user input of number of dot
        while True:
            try:
                neff = int(input("Please input the number of dots : "))
                if (neff < 2):
                    raise ValueError
            except ValueError:
                print("Please input an integer (>= 2)")
                continue
            else:
                return neff
                break
    
    def askForDimension():
        # Validate the user input of number of dimension of the dot
        while True:
            try:
                dimension = int(input("Please input the number of dimension of the dot : "))
                if (dimension < 3):
                    raise ValueError
            except ValueError:
                print("Please input an integer (>= 3)")
                continue
            else:
                return dimension
                break

    def main():
        # ============================== INPUT SEGMENT ==============================
        print("============================================================")
        print("------------ Welcome to the Closest Pair Finder ------------")

        print()
        neff = Main.askForDotNumber()       
        print()
        dimension = Main.askForDimension()
        print()

        print("------------------------------------------------------------")
        print("============================================================")
        
        # =========================== CALCULATION SEGMENT ===========================
        # Generate the dots randomly
        dotList = ListDot(dimension, neff)         
        dotList.generateRandom()

        # Divide and conquer
        startTime = time.perf_counter()
        dot1, dot2, minDist = dotList.divideAndConquer(0, dotList.neff - 1)
        endTime = time.perf_counter()

        # ============================= OUTPUT SEGMENT ==============================
        print("------------------------- Result ---------------------------")
       
        print()
        print("First dot coordinate  : ", end="")
        dot1.printDot()
        print("Second dot coordinate : ", end="")
        dot2.printDot()
        print(f"Minimal distance      : {minDist}")
        print()

        print(f"Euclidean Distance function called {dotList.euclid_count} times")
        print(f"Algorithm execution time : {endTime-startTime} seconds")
        print()

        print("------------------------------------------------------------")
        print("============================================================")


if __name__ == "__main__":
    Main.main()