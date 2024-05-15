# Python Maze Generator

This program can be used to generate a maze of any size. At some point, your computer will give up, so try and keep it under 9000.

## Usage
This project contains a Pipfile that will create a virutal python environment for you. There currently aren't any dependencies on third party libraries, but it is good to get used to working with pipenv anyways.

Clone this project, cd into the project directory, run pipenv install, then pipenv shell. Once the shell is opened, run python ./main.py --maze-size <MAZE_SIZE>

## Parameters
* --maze-size (required): The program will generate an N * N maze of this size
* --algorithm (optional): There are several ways to generate a maze. This option allows you to switch the implementation. Currently only 'backtracking' is supported.
