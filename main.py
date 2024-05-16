import argparse

from maze.generator import MazeGenerator
from printers import PrinterFactory
from utils import LOGGER

if __name__ == '__main__':
    desc = "Generates a new maze of a given size"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--maze-size', '-s', type=int, required=True, help='The size of the maze')
    parser.add_argument('--algorithm', '-a', type=str, required=False, default='backtracking',
                        help='The algorithm to use for maze generation (default: backtracking)')
    parser.add_argument('--printers', '-p', type=str, required=False, default='ascii',
                        help='The kind of printer to use to visualize the maze (default: ascii). '
                             'For more than one option, pass in a comma-separated list of printers.'
                             'Valid options: ascii, image')

    args = parser.parse_args()
    maze_size = args.maze_size
    algorithm = args.algorithm
    printers = args.printers.split(',')

    LOGGER.info(f'Generating a new maze of size {maze_size}...')
    maze_generator = MazeGenerator(maze_size, algorithm)
    maze = maze_generator.generate()
    for printer in printers:
        maze_printer = PrinterFactory.printer_factory(printer, maze)
        maze_printer.print()

    LOGGER.info('Done!')
