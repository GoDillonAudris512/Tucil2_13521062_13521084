# File          : Main.py
# Description   : For interface with user and start the algorithm to find closest pair of dots

import time
from ListDot import *
from IO import *

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
            except ValueError:
                print("Please input an integer")
                continue
            else:
                return dimension
                break
    
    def askForSaveToFile():
        # Validate the user input of option to save the answer to file or not
        while True:
            try:
                opt = input("Do you want to save your answer (Y/n): ").lower()
                if (opt != "y" and opt != "n"):
                    raise ValueError
            except ValueError:
                print("Please answer with yes (Y) or no (n)")
                continue
            else:
                return opt
                break

    def main():
        # Initialize answer string and file name
        answer = ""
        name = ""

        # ============================== INPUT SEGMENT ==============================
        print('''

 ____   ___ _____ ____    _____ ___ _   _ ____  _____ ____  
|  _ \ / _ \_   _/ ___|  |  ___|_ _| \ | |  _ \| ____|  _ \ 
| | | | | | || | \___ \  | |_   | ||  \| | | | |  _| | |_) |
| |_| | |_| || |  ___) | |  _|  | || |\  | |_| | |___|  _ < 
|____/ \___/ |_| |____/  |_|   |___|_| \_|____/|_____|_| \_\\
                                                            

        ''')
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

        # Bruteforce
        startTimeB = time.perf_counter()
        dot1, dot2, minDist1, euclidCount = dotList.bruteForce(0, dotList.neff - 1)
        endTimeB = time.perf_counter()

        # Divide and conquer
        startTimeD = time.perf_counter()
        dot3, dot4, minDist2 = dotList.divideAndConquer(0, dotList.neff - 1)
        endTimeD = time.perf_counter()

        # ============================= OUTPUT SEGMENT ==============================
        print("------------------------- Result ---------------------------")

        answer += "Result using Bruteforce Algorithm:"
        answer += "\nFirst dot coordinate  : " + dot1.writeDot()
        answer += "\nSecond dot coordinate : " + dot2.writeDot()
        answer += f"\nMinimal distance      : {minDist1}"
        answer += f"\nEuclidean Distance function called {euclidCount} times"
        answer += f"\nAlgorithm execution time : {endTimeB-startTimeB} seconds"
        
        answer += "\n\nResult using Divide and Conquer Algorithm:"
        answer += "\nFirst dot coordinate  : " + dot3.writeDot()
        answer += "\nSecond dot coordinate : " + dot4.writeDot()
        answer += f"\nMinimal distance      : {minDist2}"
        answer += f"\nEuclidean Distance function called {dotList.euclid_count} times"
        answer += f"\nAlgorithm execution time : {endTimeD-startTimeD} seconds"

        print()
        print(answer)
        print()

        if (dimension == 3) :
            dotList.plotFor3D(dot1, dot2)

        print("------------------------------------------------------------")
        print("============================================================")
        # ============================= SAVING SEGMENT ==============================
        print("------------------------- Saving ---------------------------")

        print()
        opt = Main.askForSaveToFile()
        if (opt == "y"):
            name = input("Please input the name of the file: ")
            IO.saveToFile(answer, name)

        print("\nThank you for using Closest Pair Finder")
        print("\nProcessed with : ")
        print("ASUS TUF GAMING F15")
        print("11th Gen Intel(R) Core(TM) i9-11900H @ 2.50GHz")


if __name__ == "__main__":
    Main.main()