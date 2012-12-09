import unittest

import retreat2 as life


class TestLife(unittest.TestCase):
    def setUp(self):
        self.grid = life.Grid(10)

    def test_grid_creation(self):
        self.assertEqual(len(self.grid), 10)

    def test_grid_current_position_value(self):
        self.assertEqual(self.grid[0][0], life.DEAD)

    def test_dead_or_alive(self):
        self.grid[0][1] = life.ALIVE
        self.assertEqual(self.grid[0][1], life.ALIVE)

    def test_neighbours(self):
        neighbours = self.grid.neighbours(0, 0)
        self.assertEqual(sorted(neighbours), [(0, 1), (1, 0), (1, 1)])

    def test_count_active_neighbours(self):
        self.grid[1][0] = life.ALIVE
        self.grid[1][1] = life.ALIVE
        self.assertEqual(self.grid.count_active(0, 0), 2)

    def test_tick_cell(self):
        self.grid[1][0] = life.ALIVE
        self.grid[1][1] = life.ALIVE
        cell = self.grid.tick_cell(0,0)
        self.assertEqual(cell, life.DEAD)

    def test_whole_grid(self):
        self.grid[1][0] = life.ALIVE
        self.grid[1][1] = life.ALIVE
        new_grid = self.grid.tick()
        self.assertEqual(new_grid[0][0], life.DEAD)
        self.assertEqual(new_grid[1][0], life.DEAD)

# Local Variables:
# compile-command: "python2 -m unittest test_retreat2"
# End:
