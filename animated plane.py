import os
import time


def Plane():
    distance_from_top = 25
    while True:
        print("\n" * distance_from_top)
        print("          /\          ")
        print("          ||          ")
        print("      ____||____      ")
        print("     /____||____\     ")
        print("         _||_         ")
        print("          \/          ")
        time.sleep(0.1)
        os.system('cls')
        distance_from_top -= 1
        if distance_from_top < 0:
            distance_from_top = 25


Plane()
