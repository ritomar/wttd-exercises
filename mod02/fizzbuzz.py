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

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
