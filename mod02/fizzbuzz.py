"""
Regras do Fizzbuzz
1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição: o próprio número da posição
"""

from functools import partial

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


def assert_equal(result, expeted):
    from sys import _getframe

    msg = 'Fail: Line {} got {} expecting {}'

    current_frame = _getframe()
    caller_frame = current_frame.f_back

    line_number = caller_frame.f_lineno


    if not result == expeted:
        print(msg.format(line_number, result, expeted))

if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
