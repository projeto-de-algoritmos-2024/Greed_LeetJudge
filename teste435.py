import unittest
from questao435 import Solution

class TestSolution(unittest.TestCase):

    def test_exemple_1(self):
        s = Solution()
        saida = s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
        esperado = 1
        self.assertEqual(saida, esperado)

    def test_exemple_2(self):
        s = Solution()
        saida = s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
        esperado = 2
        self.assertEqual(saida, esperado)

    def test_exemple_3(self):
        s = Solution()
        saida = s.eraseOverlapIntervals([[1,2],[2,3]])
        esperado = 0
        self.assertEqual(saida, esperado)


if __name__ == "__main__":
    unittest.main()
