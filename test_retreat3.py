import unittest

import retreat3 as life


class TestCoordinate(unittest.TestCase):
    def test_coordinate_creation(self):
        coord = life.Coordinate(0, 0)

    def test_coordinate_within_bounds(self):
        coord = life.Coordinate(0, 0)
        self.assertTrue(coord.is_within_bounds(life.Size(3)))

    def test_not_within_bounds(self):
        coord = life.Coordinate(4, 0)
        self.assertTrue(not coord.is_within_bounds(life.Size(3)))


class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        cell = life.Cell(life.ALIVE)

    def test_cell_is_alive(self):
        cell = life.Cell(life.ALIVE)
        self.assertTrue(cell.is_alive())

    def test_cell_is_dead(self):
        cell = life.Cell(life.DEAD)
        self.assertTrue(cell.is_dead())


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = life.Grid(life.Size(3))

    def test_all_dead_in_new_grid(self):
        self.assertTrue(all(x.is_dead() for x in self.grid))

    def test_cell_is_alive_after_bringing_life(self):
        coordinate = life.Coordinate(0, 0)
        self.grid.bring_to_life(coordinate)
        self.assertTrue(self.grid.get(coordinate).is_alive())

    def test_middle_element_has_8_neighbours(self):
        coord = life.Coordinate(1, 1)
        self.assertEqual(len(self.grid.neighbours(coord)), 8)
