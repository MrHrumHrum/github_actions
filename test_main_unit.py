import unittest
from main import main


class CalculateAverageTestCase(unittest.TestCase):
    # Только положительные числа
    def test_only_pos_1(self):
        res = main([10, 3, 2])
        self.assertEqual(res, 5)

    def test_only_pos_2(self):
        res = main([1, 3, 4])
        self.assertEqual(res, 2.67)

    # Только отрицательные числа
    def test_only_neg_1(self):
        res = main([-1, -2, -3])
        self.assertEqual(res, -2)

    def test_only_neg_2(self):
        res = main([-7, -2, -1, -2])
        self.assertEqual(res, -3)

    # Пустой список
    def test_none(self):
        res = main([])
        self.assertEqual(res, None)