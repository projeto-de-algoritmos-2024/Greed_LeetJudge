import unittest
from questao632 import Solution

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_smallestRange_1(self):
        nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        expected_range = [20, 24]
        self.assertEqual(self.solution.smallestRange(nums), expected_range)

    def test_smallestRange_2(self):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected_range = [1, 1]
        self.assertEqual(self.solution.smallestRange(nums), expected_range)

    def test_smallestRange_3(self):
        nums = [[10, 10], [11, 11]]
        expected_range = [10, 11]
        self.assertEqual(self.solution.smallestRange(nums), expected_range)

    def test_smallestRange_4(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_range = [3, 7]
        self.assertEqual(self.solution.smallestRange(nums), expected_range)

if __name__ == "__main__":
    unittest.main()
