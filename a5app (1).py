"""User interface script for the module a5.

Asks the user for the seed number to use, and the width and height of Conway's
game of life board

When both inputs are valid, creates a random board of requested width and height,
and calculates the first 100 generations, printing out each generation.

AUTHOR: tbg35 lnp29
"""
import a5
import time

print('Hello Player, welcome to Conways game of life!')
height = int(input('Please enter the desired height of the game board: '))
width = int(input('Please enter the desired width of the game board: '))
seed = int(input('Please enter a choice number to seed the randomization of the'
+' game board: '))
print('All parameters received. Now generating you 100 boards of Conway\'s game'
+' of life')
game = a5.Life(width, height)
game.randomize(seed)
game.print()
for i in range(99):
    time.sleep(0.5)
    game.next()
    game.print()
