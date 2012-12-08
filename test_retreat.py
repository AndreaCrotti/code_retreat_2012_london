import unittest
import retreat


class TestLife(unittest.TestCase):
    def test_empty_grid(self):
        grid = retreat.Grid(4, state=False)
        self.assertEqual(grid[0][0], retreat.Cell(False))

    def test_simple_grid(self):
        grid = retreat.Grid(4, state=True)
        grid[0][1] = retreat.Cell(False)
        self.assertEqual(grid[0][1], False)

    def test_neighbour_middle(self):
        grid = retreat.Grid(3, state=True)
        neigh_middle = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(sorted(grid.neighbours(1, 1)), sorted(neigh_middle))

    def test_neighbour_corner(self):
        grid = retreat.Grid(3, state=True)
        neigh_zero = [(0, 1), (1, 0), (1, 1)]
        self.assertEqual(sorted(grid.neighbours(0, 0)), neigh_zero)
        neigh_one_zero = [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]
        self.assertEqual(sorted(grid.neighbours(1, 0)), neigh_one_zero)
