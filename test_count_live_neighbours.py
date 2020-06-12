import unittest

import model

cell = model.cell


class test_count_live_neighbours(unittest.TestCase):

    def test_dead_cell(self):
        grid = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
        self.assertEqual(model.countLiveNeighbours(0, 0, grid, 3, 3), 2)

    def test_live_cell(self):
        grid = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
        self.assertEqual(model.countLiveNeighbours(1, 1, grid, 3, 3), 2)

    def test_live_cell_two(self):
        grid = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
        self.assertEqual(model.countLiveNeighbours(2, 1, grid, 3, 3), 1)


if __name__ == '__main__':
    unittest.main()
