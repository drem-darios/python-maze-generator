class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

    def visit(self):
        self.visited = True
