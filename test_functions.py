from functions import sum_number
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(30, sum_number(10,20))

    def test_sum_two(self):
        self.assertEqual(60, sum_number(30, 30))

    def test_sum_three(self):
        self.assertEqual(100, sum_number(50, 50))
    
    def test_full_name(self):
        self.assertEqual("Santiago, Gonzalez", get_full_name("gonzalez","santiago"))

if __name__ == '__main__':
    unittest.main()
