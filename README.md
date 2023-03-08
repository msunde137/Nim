# 107project-tripeny-sunde-katz

## Build Instructions

This game requires [Python](https://Python.org), [PyGame](https://www.pygame.org/), and [NumPy](https://numpy.org/).

To play the game, download the project files and run using the terminal command ```python Game.py```

## About

  We will be examining the classic game Nim and how it can be implemented in Python. This will include a user interface to play 
these games. 

  The game nim can be implemented using a list. The game has n different "piles", each with a positive number of coins. Two 
players alternate taking turns, each player removing any number of coins from exactly one pile. For example, one may move the 
board [3, 5, 7] to the board [3, 2, 7] by removing 3 coins from pile 2. However, one may not move the board [3, 5, 7] to
[1, 3, 7] because multiple columns are changed. A player wins when they move to a zero board, [0, 0, 0] such that the other 
player can't remove any coins. 

  After implementing nim, we could explore other game formats using different data structures. Fore example, using a set, the 
board {3, 5, 7} could be changed to {3, 5, 5}, but since sets have no unique elements this is {3, 5}. 

  The game could also be implemented using queue, stack, or priority queue. Each different implementation would have have 
different strategies. Examing the game structure and the winning strategy can help students to understand the differences 
between various data structures.

Sources:
https://arxiv.org/pdf/1605.06327.pdf
This source describes the game and certain strategies, but has no code to play the games. 
