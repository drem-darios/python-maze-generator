from abc import abstractmethod, ABC


class MazePrinter(ABC):
    def __init__(self, maze):
        self.maze = maze
        super().__init__()

    @abstractmethod
    def print(self):
        pass


class ASCIIPrinter(MazePrinter):
    def __init__(self, maze):
        super().__init__(maze)

    def print(self):
        for i in range(self.maze.size):
            # Draw top walls
            for j in range(self.maze.size):
                if self.maze.grid_walls[i][j]['top']:
                    print("+---", end="")
                elif i == 0 and j == 0:
                    print("+ S ", end="")
                else:
                    print("+   ", end="")
            print("+")

            # Draw left and right walls
            for j in range(self.maze.size):
                if self.maze.grid_walls[i][j]['left']:
                    print("|", end="")
                print("   " if self.maze.grid_walls[i][j]['right'] else "    ", end="")
            print("|")

        # Draw bottom walls
        for j in range(self.maze.size):
            print("+ E " if (j == self.maze.size - 1) else "+---", end="")
        print("+")
