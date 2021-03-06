"""Module to simulate Conway's Game of Life.

This module holds the class Life, which can be used to simulate the board
states in Conway's Game of Life, one generation at a time.

AUTHOR: Lucas Paschke
"""

import random


class Life:
    """Describes the world of Conway's Game of Life.

    Attribute width: the width of the game world in number of cells.
    Invariant: width is a non-negative integer.

    Attribute height: the height of the game world in number of cells.
    Invariant: height is a non-negative integer.

    Attribute board: the board of the game world.
    Invariant: board is a two-dimensional list of booleans in column-major
    order, of the height and width as specified in the attributes. The value
    True represents a live cell, False represents a dead cell.
    """

    def __init__(self, width, height):
        """Initializes the Game of Life with the given width and height.

        Also initializes the attribute board to be of the right size, and with
        all cells dead.

        Precondition: width and height are nonnegative integers.
        """

        assert width > 0, 'width is a negative number'
        assert height > 0, 'height is a negative number'
        assert type(width) == int, 'width is not an integer'
        assert type(height) == int, 'height is not an integer'
        self.height = height
        self.width = width

        self.board = []
        for x in range(width):
            self.board.append([False]*height)

    def randomize(self, seed_number):
        """Randomizes the current state of the Game of Life with the seed
        number given in the parameter seed_number.

        Precondition: seed_number is an int.
        """
        assert type(seed_number) == int, 'the seed is not an integer'
        random.seed(seed_number)
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # could also use random.choice([True, False]) or
                #random.randint(0, 1) == 1
                self.board[x][y] = bool(random.randint(0, 1))

    def count_neighbors(self, x, y):
        """Counts the number of live neighbors of the cell at (x, y).

        Precondition: x is an int, at least 0 and at most width-1; similarly,
        y is an int, at least 0 and at most height-1.
        """

        assert type(x)==int, 'x should be an integer'
        assert x>=0, 'x should be at least zero'
        assert type(y)==int, 'y should be an integer '
        assert y>=0, 'y should be at least 0'
        assert x<=self.width-1, 'x should be at most width-1'
        assert y<=self.height-1, 'y should be at most height-1'

        live_neighbors=0

        if x-1>=0 and y-1>=0 and self.board[x-1][y-1]:
            live_neighbors=live_neighbors+1

        if x-1>=0 and self.board[x-1][y]:
            live_neighbors=live_neighbors+1

        if x-1>=0 and y+1<self.height and self.board[x-1][y+1]:
            live_neighbors=live_neighbors+1
        if y-1>=0 and self.board[x][y-1]:
            live_neighbors=live_neighbors+1

        if y+1<self.height and self.board[x][y+1]:
            live_neighbors=live_neighbors+1

        if x+1<self.width and y-1>=0 and self.board[x+1][y-1]:
            live_neighbors=live_neighbors+1

        if x+1<self.width and self.board[x+1][y]:
            live_neighbors=live_neighbors+1

        if x+1<self.width and y+1<self.height and self.board[x+1][y+1]:
            live_neighbors=live_neighbors+1

        return live_neighbors

    def next(self):
        """Calculates the next generation and stores it in the attribute board
        of the current instance of Life.

        The rules to calculate the next generation were described in detail in
        the assignment description that you were given.
        """
        next_board = []
        for t in range(self.width):
            next_board.append([False]*self.height)

        for x in range(self.width):
            for y in range(self.height):
                    alive=self.count_neighbors(x,y)
                    cell=self.board[x][y]
                    #Loneliness
                    if cell==True and alive<2:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=False
                    #Happiness
                    elif cell==True and alive==2:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=True
                    #Happiness Two
                    elif cell==True and alive==3:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=True
                    #Overcrowding
                    elif cell==True and alive>3:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=False
                    #Reproduction
                    elif cell==False and alive==3:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=True
                    #Stasis
                    elif cell==False and alive>3:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=False
                    #Stasis 2
                    elif cell==False and alive<3:
                        del next_board[x][0]
                        next_board[x].append(cell)
                        next_board[x][self.height-1]=False

        self.board=next_board



    def print(self):
        """Prints the current state of the board to the output.

        The character 'x' represents a live cell, while the character ' ' (a
        single space!) represents a dead cell.

        Remember the convention we adopted at the beginning of the exercise,
        that told you how the coordinates of the grid were laid out.
        """
        for y in range(len(self.board[0])):
            temp_str = ''
            for x in range(len(self.board)):
                if self.board[x][y]:
                    temp_str += 'x'
                else:
                    temp_str += ' '
            print(temp_str) #can also append new lines via \n and move temp_str
                            #out of loop
