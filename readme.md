# Tic Tac Toe Me

## Summary

A simple command line python implementation
of the game Tic Tac Toe

## Directions
Python version 3.7

No additional external dependencies are required

To run the application, execute the file `main.py`
either through command line or using an IDE

Files have been formatted using a default [Black formatter](https://github.com/psf/black) configuration

## Details
The application is split into different components
that represent the various parts of a typical Tic Tac Toe.

The player is able to choose which symbol 
they would like to be between X and O at the beginning of the program.

The game will then begin and ask the user to choose a cell to fill.
The board and corresponding cells can be represented as follows:

```
1|2|3
4|5|6
7|8|9
 ```
Player and AI turns will alternate until the process is terminated.

AI player will alternate with a 50/50 split between two different
strategies for determining the next move:
* random selection based on available empty cells
* the best possible move based on minimax algorithm with alpha/beta pruning.
  Total look-ahead depth is determined randomly between 2 and 6
  
I had a lot of fun creating this little game, hope you like it!