"""
Regras do Fizzbuzz
1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição: o próprio número da posição
"""

from functools import partial
import unittest


is_divisible = lambda a, b: b % a == 0
is_divisible_by_3 = partial(is_divisible, 3)
is_divisible_by_5 = partial(is_divisible, 5)


def robot(position):
    if is_divisible_by_3(position) and is_divisible_by_5(position):
        robotSay = 'fizzbuzz'
    elif is_divisible_by_5(position):
        robotSay = 'buzz'
    elif is_divisible_by_3(position):
        robotSay = 'fizz'
    else:
        robotSay = str(position)

    return robotSay


class FizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')


    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')


    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')


    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')


    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')


    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')


    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')


    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')


    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20), 'buzz')


    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')


    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(robot(30), 'fizzbuzz')


    def test_say_fizzbuzz_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
