from katas import kata11
import unittest  

class Test_Sort(unittest.TestCase):
    def test_sort(self):
        res = kata11.sort("Hello world!")
        self.assertEqual(res, "dehllloorw")

if __name__ == '__main__':
    unittest.main()