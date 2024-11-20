from solution import get_wiki
import unittest
import csv


class WikiTest(unittest.TestCase):
    def test_load(self):
        all_category = get_wiki()
        with open('beasts.csv', 'r') as f:
            reader = csv.reader(f)
            result = dict(reader)

        # self.assertEqual(all_category, 46_290)
        self.assertEqual(int(result['Ё']), 2)
        self.assertEqual(int(result['Z']), 231)


if __name__ == '__main__':
    unittest.main()

