from abc import abstractmethod, ABC
from PIL import Image, ImageDraw


class MazePrinter(ABC):
    def __init__(self, maze):
        self.maze = maze
        super().__init__()

    @abstractmethod
    def print(self):
        pass


class PrinterFactory(object):
    @staticmethod
    def printer_factory(printer, maze) -> MazePrinter:
        if printer == 'ascii':
            return ASCIIPrinter(maze)
        elif printer == 'image':
            return ImagePrinter(maze)
        else:
            raise ValueError(f"Invalid printer type: {printer}")


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


class ImagePrinter(MazePrinter):
    def __init__(self, maze):
        super().__init__(maze)
        self.cell_size = 40
        self.wall_thickness = 3
        self.image_size = (self.maze.size * self.cell_size) + self.wall_thickness

    def print(self):
        img = Image.new('RGB', (self.image_size, self.image_size), 'white')
        draw = ImageDraw.Draw(img)

        for i in range(self.maze.size):
            for j in range(self.maze.size):
                x = j * self.cell_size
                y = i * self.cell_size

                # Draw top wall
                if self.maze.grid_walls[i][j]['top']:
                    draw.line((x, y, x + self.cell_size, y), fill="black", width=self.wall_thickness)

                # Draw left wall
                if self.maze.grid_walls[i][j]['left']:
                    draw.line((x, y, x, y + self.cell_size), fill="black", width=self.wall_thickness)

                # Draw right wall if it's the last column or if there's a right wall
                if j == self.maze.size - 1 or self.maze.grid_walls[i][j]['right']:
                    draw.line((x + self.cell_size, y, x + self.cell_size, y + self.cell_size), fill="black",
                              width=self.wall_thickness)

                # Draw bottom wall if it's the last row or if there's a bottom wall
                if i == self.maze.size - 1 and self.maze.grid_walls[i][j]['bottom']:
                    draw.line((x, y + self.cell_size, x + self.cell_size, y + self.cell_size), fill="black",
                              width=self.wall_thickness)

        # Draw the start
        draw.text((self.cell_size // 3, self.cell_size // 4), "S", fill="green", font_size=20)

        # Draw the exit
        ex = (self.maze.size - 1) * self.cell_size
        ey = (self.maze.size - 1) * self.cell_size
        draw.text((ex + self.cell_size // 3, ey + self.cell_size // 4), "E", fill="red", font_size=20)

        img.show()
        img.save("maze.png")
