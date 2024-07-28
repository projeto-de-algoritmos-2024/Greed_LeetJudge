import unittest
from questao2136 import Solution

class TestSolution(unittest.TestCase):

    def test_exemple_1(self):
        s = Solution()
        saida = s.earliestFullBloom([1,4,3],[2,3,1])
        esperado = 9
        self.assertEqual(saida, esperado)

    def test_exemple_2(self):
        s = Solution()
        saida = s.earliestFullBloom([1,2,3,2],[2,1,2,1])
        esperado = 9
        self.assertEqual(saida, esperado)

    def test_exemple_3(self):
        s = Solution()
        saida = s.earliestFullBloom([1],[1])
        esperado = 2
        self.assertEqual(saida, esperado)


if __name__ == "__main__":
    unittest.main()
