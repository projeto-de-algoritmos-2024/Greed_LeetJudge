import unittest
from qquestao621 import Solution

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_leastInterval_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected_intervals = 8
        self.assertEqual(self.solution.leastInterval(tasks, n), expected_intervals)

    def test_leastInterval_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected_intervals = 6
        self.assertEqual(self.solution.leastInterval(tasks, n), expected_intervals)

    def test_leastInterval_3(self):
        tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"]
        n = 2
        expected_intervals = 10
        self.assertEqual(self.solution.leastInterval(tasks, n), expected_intervals)

    def test_leastInterval_4(self):
        tasks = ["A", "A", "A", "B", "B", "C"]
        n = 2
        expected_intervals = 7
        self.assertEqual(self.solution.leastInterval(tasks, n), expected_intervals)

if __name__ == "__main__":
    unittest.main()
