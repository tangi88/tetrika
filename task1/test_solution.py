from solution import strict
import unittest


class StrictTest(unittest.TestCase):
    def test_value(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two_str('1', '2'), '12')
        self.assertEqual(sum_two_float(1.0, 2.0), 3.0)
        self.assertEqual(sum_two_bool(True, True), 2)
        self.assertEqual(sum_all(1, 2, 3), 6)
        self.assertEqual(sum_three(1, 2, 3, 4), 10)
        self.assertEqual(sum_two_str('1', '23'), '123')

    def test_raise(self):
        self.assertRaises(TypeError, sum_two, 1, False)
        self.assertRaises(TypeError, sum_two_and_float, 1, 2)
        self.assertRaises(TypeError, sum_two_str, 1, '')
        self.assertRaises(TypeError, sum_two_float, 1, 1.0)
        self.assertRaises(TypeError, sum_two_bool, True, 1)
        self.assertRaises(TypeError, sum_all, 1, 2, 5.6, 6)
        self.assertRaises(TypeError, sum_three, "1", 2)
        self.assertRaises(TypeError, sum_three, 1, 2, 3, 4.6)


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_and_float(a: int, b: int) -> int:
    return a + b + 0.1


@strict
def sum_two_str(a: str, b: str) -> str:
    return a + b


@strict
def sum_two_float(a: float, b: float) -> float:
    return a + b


@strict
def sum_two_bool(a: bool, b: bool) -> int:
    return a + b


@strict
def sum_all(*args: int) -> int:
    return sum(args)


@strict
def sum_three(a: int, b: int, *args: int) -> int:
    return a + b + sum(args)


if __name__ == '__main__':
    unittest.main()

