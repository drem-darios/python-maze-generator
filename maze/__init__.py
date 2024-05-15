from maze.point import Point


class Maze(object):
    def __init__(self, maze_size):
        self.size = maze_size
        self.grid = [[Point(x, y) for y in range(maze_size)] for x in range(maze_size)]
        self.grid_path = []
        self.grid_walls = [[{'top': True, 'right': True, 'bottom': True, 'left': True} for _ in range(maze_size)] for _
                           in range(maze_size)]

    def find_connections(self, x, y) -> list[Point]:
        connections = []
        if x > 0:
            connections.append(self.grid[x - 1][y])
        if y > 0:
            connections.append(self.grid[x][y - 1])
        if x < self.size - 1:
            connections.append(self.grid[x + 1][y])
        if y < self.size - 1:
            connections.append(self.grid[x][y + 1])
        return connections

    def initialize_maze(self, path):
        self.grid_path = path
        # Go through grid walls and remove all the walls between the points in the path
        for i in range(len(path) - 1):
            if path[i].x == path[i + 1].x:
                if path[i].y < path[i + 1].y:
                    self._remove_walls(path[i].x, path[i].y, 'right')
                    self._remove_walls(path[i + 1].x, path[i + 1].y, 'left')
                else:
                    self._remove_walls(path[i].x, path[i].y, 'left')
                    self._remove_walls(path[i + 1].x, path[i + 1].y, 'right')
            if path[i].y == path[i + 1].y:
                if path[i].x < path[i + 1].x:
                    self._remove_walls(path[i].x, path[i].y, 'bottom')
                    self._remove_walls(path[i + 1].x, path[i + 1].y, 'top')
                else:
                    self._remove_walls(path[i].x, path[i].y, 'top')
                    self._remove_walls(path[i + 1].x, path[i + 1].y, 'bottom')
        self._set_entrance()
        self._set_exit()

    def _remove_walls(self, x, y, wall):
        self.grid_walls[x][y][wall] = False

    def _set_entrance(self):
        self.grid_walls[0][0]['top'] = False

    def _set_exit(self):
        self.grid_walls[self.size - 1][self.size - 1]['bottom'] = False
