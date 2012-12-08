__metaclass__ = type

from copy import deepcopy


class Grid:
    def __init__(self, length):
        self.length = length
        self.grid = []
        for i in range(self.length):
            self.grid.append([])
            for j in range(self.length):
                self.grid[i].append(0)

    def __len__(self):
        return self.length

    def __str__(self):
        line = lambda l: ' '.join(str(x) for x in l)
        return '\n'.join(line(x) for x in self.grid)

    def __getitem__(self, item):
        return self.grid[item]

    def _is_valid_neigh(self, x, y):
        valid = lambda x: (x >= 0) and (x < self.length)
        return valid(x) and valid(y)

    def neighbours(self, x, y):
        upper = [(x-1, j) for j in range(y-1, y+2)]
        lower = [(x+1, j) for j in range(y-1, y+2)]
        lr = [(x, y-1), (x, y+1)]
        all_neigh = lower + upper + lr
        res = []
        for n in all_neigh:
            if self._is_valid_neigh(n[0], n[1]):
                res.append(n)

        return res

    def count_active(self, x, y):
        res = self.neighbours(x,y)
        active_neigh = [x for x in res if self.grid[x[0]][x[1]] == 1]
        return len(active_neigh)

    def tick_cell(self, x, y):
        active = self.count_active(x, y)
        if (active == 2) or (active == 3):
            return 1
        else:
            return 0

    def tick(self):
       matrix = deepcopy(self.grid)
       new_grid = Grid(self.length)
       new_grid.grid = matrix
       for i in range(self.length):
           for j in range(self.length):
               val = self.tick_cell(i, j)
               new_grid[i][j] = val

       return new_grid


if __name__ == '__main__':
    grid = Grid(10)
    grid[1][0] = 1
    grid[1][1] = 1
    print(grid)
    print("---")
    print(grid.tick())

# Local Variables:
# compile-command: "python2 -m unittest test_retreat2"
# End:
