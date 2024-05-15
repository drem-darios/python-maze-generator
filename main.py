import argparse

from maze.generator import MazeGenerator
from printers import ASCIIPrinter
from utils import LOGGER

if __name__ == '__main__':
    desc = "Generates a new maze of a given size"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--maze-size', '-s', type=int, required=True, help='The size of the maze')
    parser.add_argument('--algorithm', '-a', type=str, required=False, default='backtracking',
                        help='The algorithm to use for maze generation (default: backtracking)')

    args = parser.parse_args()
    maze_size = args.maze_size
    algorithm = args.algorithm

    LOGGER.info(f'Generating a new maze of size {maze_size}...')
    maze_generator = MazeGenerator(maze_size, algorithm)
    maze = maze_generator.generate()

    maze_printer = ASCIIPrinter(maze)
    maze_printer.print()
    
    LOGGER.info('Done!')
