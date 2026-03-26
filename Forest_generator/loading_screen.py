import os
import time
import random
import sys
from Forest_generator.forest import Forest
from Forest_generator.tree import Tree
import Forest_generator.loading_text as loadingText


class LoadingScreen:
    #Intial screen clear function
    os.system("cls" if os.name == "nt" else "clear")

    #Forest dimensions
    WIDTH = 190
    HEIGHT = 20
    forest = Forest(cols=WIDTH, rows=HEIGHT)

    #Amount of trees to generate
    for _ in range(45):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        forest.place(Tree(), x, y)

    #Main loop to grow trees and display the forest
    for _ in range(5):
        loadingText.game_title()
        if _ == 0:
            loadingText.loading_text()
        forest.grow()
        print(forest)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

    #Calling the main Home screen function with rules
    loadingText.cabin()

