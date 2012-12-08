__metaclass__ = type


DEAD = "_"
ALIVE = "o"


class Cell:
    def __init__(self, state):
        self.state = state

    def is_alive(self):
        return self.state == ALIVE

    def is_dead(self):
        return self.state == DEAD


class Grid:
    def __init__(self, size):
        self.cells = []
        for i in range(size.size):
            self.cells.append([])
            for j in range(size.size):
                self.cells[i].append(Cell(DEAD))

    def __iter__(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                yield self.cells[i][j]

    def get(self, coordinate):
        return self.cells[coordinate.x][coordinate.y]

    def bring_to_life(self, coordinate):
        self.cells[coordinate.x][coordinate.y] = Cell(ALIVE)

    def kill(self, coordinate):
        self.cells[coordinate.x][coordinate.y] = Cell(DEAD)

    def neighbours(self, coordinate):
        upper = [Coordinate(x-1, y) for y in range(coordinate.y-1, coordinate.y+2)]
        lower = [Coordinate(x+1, y) for y in range(coordinate.y-1, coordinate.y+2)]
        left_and_right = [Coordinate(coordinate.x, coordinate.y - 1), Coordinate(coordinate)]   


class Size:
    def __init__(self, size):
        self.size = size


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_within_bounds(self, length):
        return (self.x >= 0) and (self.x < length.size) and \
          (self.y >= 0) and (self.y < length.size)
