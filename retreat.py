__metaclass__ = type

import numpy as np
from random import choice


class Cell:
    def __init__(self, state=None):
        if state is not None:
            self.state = state
        else:
            self.state = choice((True, False))

    def die(self):
        self.state = False

    def revive(self):
        self.state = True

    def __eq__(self, other):
        if type(other) == bool:
            return self.state == other
        else:
            return self.state == other.state

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.state:
            return 'o'
        else:
            return ' '

class Grid:
    def __init__(self, dim, state=None):
        self.dim = dim
        self.grid = []
        for i in range(self.dim):
            self.grid.append([])
            for j in range(self.dim):
                self.grid[i].append(Cell(state))

    def __str__(self):
        line_str = lambda l: ' '.join(str(c) for c in l)
        return '\n'.join(line_str(x) for x in self.grid)

    def filter_out(self, all_neigh):
        res = []
        valid = lambda x: (x >= 0) and (x < self.dim)
        for neigh in all_neigh:
            if valid(neigh[0]) and valid(neigh[1]):
                res.append(neigh)

        return res

    def neighbours(self, x, y):
        """Return list of neighbour cells
        """
        upper = [(x-1, j) for j in range(y-1, y+2)]
        lower = [(x+1, j) for j in range(y-1, y+2)]
        l_r = [(x, y-1), (x, y+1)]
        all_neighbours = upper + lower + l_r
        return self.filter_out(all_neighbours)

    def __getitem__(self, item):
        return self.grid[item]

    def tick_cell(self, x, y):
        neighbours = self.neighbours(x, y)
        num_neigh_on = len(filter(lambda x: x == True, neighbours))
        if num_neigh_on < 2:
            pass

    def tick(self):
        pass


if __name__ == '__main__':
    g = Grid(10)
    print(g)
    g2 = Grid(10, False)
    print(g2)
