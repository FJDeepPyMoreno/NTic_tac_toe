# NTic_tac_toe
Simulation of a random tic-tac-toe game in N-sized boards.

The purpose of Ntictactoe.py module is to play simulating tic-tac-toe games using an arbitrary N x N sized boards.

The way to use it is as follows:

import Ntictactoe

(I like to use: import Ntictactoe as Nttt , or import Ntictactoe as ttt)
Ntictactoe.py contents

    class TableroNR: it represents a N x N board, where tokens of two different kinds play a N-tictactoe game. By N-tictactoe, I mean that you win if you complete a (horizontal, vertical or diagonal) line of N-length.

    runtableroNR function: simulates a Ntictactoe game a number of times and creates an output file which stores the resuts of the game. The output file (.csv) stores the following data for each simulation game: Board size, Iteration number, Number of tokens on the board when anyone wins, type of line (D: diagonal, V: vertical, H: horizontal) that won (if nobody won, it takes 'N')

    nboard_generator function: calls 'runtableroNR' function using borards of different size. This is the proper function to generate in one execution different files in order to compare the effects of board size.

Results

Results can be seen in output.csv files and .png files. The displayed results correspond to data generated from 5000 games for each board from size 3x3 to size 10x10.

These data has been manipulated using numpy, seaborn, matplotlib and pandas libraries. See jupyter notebook file: 'data_Ntictactoe.ipynb'

