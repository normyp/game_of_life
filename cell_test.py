import unittest
import model

class TestCell(unittest.TestCase):

    def test_dead_cell_with_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 3}
        model.generate(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_zero_neighbours(self):
        c = {"status": '0', "cell_neighbours": 0}
        model.generate(c)
        self.assertEqual(c["status"], '0')

    def test_dead_cell_with_more_than_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 4}
        model.generate(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_zero_neighbours(self):
        c = {"status": '1', "cell_neighbours": 0}
        model.generate(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_two_neighbours(self):
        c = {"status": '1', "cell_neighbours": 2}
        model.generate(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_three_neighbours(self):
        c = {"status": '0', "cell_neighbours": 3}
        model.generate(c)
        self.assertEqual(c["status"], '1')

    def test_dead_cell_with_two_neighbours(self):
        c = {"status": '0', "cell_neighbours": 2}
        model.generate(c)
        self.assertEqual(c["status"], '0')

    def test_live_cell_with_one_neighbour(self):
        c = {"status": '1', "cell_neighbours": 1}
        model.generate(c)
        self.assertEqual(c["status"], '0')


    def test_cell(self):
        test_cases = [
            {
                "name": "test live cell with more than three neighbours",
                "input": {"status": '1', "cell_neighbours": 4},
                "expected": '0'
            },
            {
                "name": "test_live_cell_with_three_neighbours",
                "input": {"status": '1', "cell_neighbours": 3},
                "expected": '1'
            }
        ]
        for test_case in test_cases:
            c = test_case["input"]
            model.generate(c)
            self.assertEqual(c["status"], test_case["expected"], test_case["name"])

if __name__ == '__main__':
    unittest.main()
