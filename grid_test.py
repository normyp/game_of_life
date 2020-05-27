import unittest
import model

class TestGrid(unittest.TestCase):

    def test_empty_grid(self):
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        grid = model.generate(grid)
        self.assertEqual(grid, [[0,0,0],[0,0,0],[0,0,0]])

    def test_horizontal_three(self):
        grid = [[0,0,0],[1,1,1],[0,0,0]]
        grid = model.generate(grid)
        self.assertEqual(grid, [[0,1,0],[0,1,0],[0,1,0]])

if __name__ == '__main__':
    unittest.main()
