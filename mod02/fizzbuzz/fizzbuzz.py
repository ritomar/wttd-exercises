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

