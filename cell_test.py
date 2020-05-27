import unittest
import model

class TestCell(unittest.TestCase):

    def test_dead_cell_with_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 3}
        model.is_alive(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_zero_neighbours(self):
        c = {"status": '0', "cell_neighbours": 0}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

    def test_dead_cell_with_more_than_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 4}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_zero_neighbours(self):
        c = {"status": '1', "cell_neighbours": 0}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_two_neighbours(self):
        c = {"status": '1', "cell_neighbours": 2}
        model.is_alive(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 3}
        model.is_alive(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_two_neighbours(self):
        c = {"status": '0', "cell_neighbours": 2}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_one_neighbour(self):
        c = {"status": '1', "cell_neighbours": 1}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_three_neighbours(self):
        c = {"status": '1', "cell_neighbours": 3}
        model.is_alive(c)
        self.assertEqual(c["status"], '1')

    def test_live_cell_with_more_than_three_neighbours(self):
        c = {"status": '1', "cell_neighbours": 4}
        model.is_alive(c)
        self.assertEqual(c["status"], '0')

if __name__ == '__main__':
    unittest.main()
