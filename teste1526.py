import unittest
from questao1526 import Solution

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_minNumberOperations_1(self):
        target = [1,2,3,2,1]
        expected_operations = 3
        self.assertEqual(self.solution.minNumberOperations(target), expected_operations)

    def test_minNumberOperations_2(self):
        target = [3, 1,1,2]
        expected_operations = 4
        self.assertEqual(self.solution.minNumberOperations(target), expected_operations)

    

if __name__ == "__main__":
    unittest.main()
