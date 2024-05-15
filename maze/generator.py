from algorithms import Backtracking, MazeAlgorithm
from maze import Maze


class MazeGenerator(object):
    def __init__(self, maze_size=10, generator_type="backtracking"):
        self.maze = Maze(maze_size)
        self.generator = self._get_generator(generator_type)

    def generate(self) -> Maze:
        self.generator.generate()
        return self.maze

    def _get_generator(self, generator_type) -> MazeAlgorithm:
        if generator_type == 'backtracking':
            return Backtracking(self.maze)
        else:
            raise ValueError(f'Invalid generator type: {generator_type}')
