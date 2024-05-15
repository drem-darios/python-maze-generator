import copy
import random
from abc import ABC, abstractmethod

from utils import LOGGER


class MazeAlgorithm(ABC):
    def __init__(self, maze):
        self.maze = maze
        super().__init__()

    @abstractmethod
    def generate(self):
        pass


class Backtracking(MazeAlgorithm):
    def __init__(self, maze):
        super().__init__(maze)

    def generate(self):
        self._generate(0, 0)

    def _generate(self, starting_x, starting_y):
        curr_x, curr_y = starting_x, starting_y
        maze_grid = copy.deepcopy(self.maze.grid)
        maze_grid[curr_x][curr_y].visit()
        path = [maze_grid[curr_x][curr_y]]
        visit_counter = 1
        visited_points = []

        while visit_counter < (self.maze.size * self.maze.size):
            connections = self.maze.find_connections(curr_x, curr_y)
            unvisited_connections = [maze_grid[connection.x][connection.y] for connection in connections if
                                     not maze_grid[connection.x][connection.y].visited]

            if unvisited_connections:
                visited_points.append(maze_grid[curr_x][curr_y])  # Add current point to stack
                next_point = random.choice(unvisited_connections)  # Choose a random connection to move to
                curr_x, curr_y = next_point.x, next_point.y
                maze_grid[curr_x][curr_y].visit()
                path.append(maze_grid[curr_x][curr_y])
                visit_counter += 1

            elif len(visited_points) > 0:  # If there are points that still need to be visited, backtrack
                previous_point = visited_points.pop()
                curr_x, curr_y = previous_point.x, previous_point.y
                path.append(previous_point)

        LOGGER.info(f"Generated path length: {len(path)}")
        self.maze.initialize_maze(path)
