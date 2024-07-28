import unittest
from questao452 import Solution

class TestSolution(unittest.TestCase):

    def test_exemple_1(self):
        s = Solution()
        saida = s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
        esperado = 2
        self.assertEqual(saida, esperado)

    def test_exemple_2(self):
        s = Solution()
        saida = s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        esperado = 4
        self.assertEqual(saida, esperado)

    def test_exemple_3(self):
        s = Solution()
        saida = s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
        esperado = 2
        self.assertEqual(saida, esperado)


if __name__ == "__main__":
    unittest.main()
