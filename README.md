# Python Maze Generator

This program can be used to generate a maze of any size. At some point, your computer will give up, so try and keep it under 1000 for now.

## Usage
This project contains a Pipfile that will create a virtual python environment and install dependencies for you.
To run this project locally, clone this project and do the following steps: 

1. Run `cd python-maze-generator`
2. Run `pipenv install` to create the virtual environment and install dependencies
3. Run `pipenv shell` to open a python shell in the virtual environment
4a. Run `python ./main.py --maze-size <MAZE_SIZE>` to generate a maze with the given size
4b. Run `python ./main.py --maze-size <MAZE_SIZE> --printers image` to generate an image of the maze
4c. Run `python ./main.py --maze-size <MAZE_SIZE> --printers ascii,image` to generate both an image and print the maze as ascii to the console

## Parameters
* --maze-size (required): The program will generate an N * N maze of this size
* --algorithm (optional): There are several ways to generate a maze. This option allows you to switch the implementation. Currently only 'backtracking' is supported.
* --printers (optional): This option allows you to switch the way the maze is printed. Currently 'ascii' (default) and 'image' are supported. Pass in a comma separated list to use multiple printers.
