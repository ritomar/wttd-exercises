def roman_to_decimal(value):

    basic_convert = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    digits = []
    for v in value:
        if v in basic_convert.keys():
            digits.append(basic_convert[v])

    i = len(digits) - 1
    while i >= 0:
        if (i > 0) and (digits[i] in [5, 10, 50, 500]) and digits[i] > digits[i - 1]:
            while i > 0 and digits[i - 1] in [1, 10, 100, 1000]:
                if digits[i - 1] >= digits[i]:
                    digits[i - 1] *= -1
                    i -= 1
                else:
                    digits[i - 1] *= -1
                    i -= 1
                    break
        else:
            i -= 1

    print('Romano:', value, 'Digitos:',digits, '=', sum(digits))
    return sum(digits)

assert roman_to_decimal('I') == 1
assert roman_to_decimal('V') == 5
assert roman_to_decimal('X') == 10
assert roman_to_decimal('L') == 50
assert roman_to_decimal('C') == 100
assert roman_to_decimal('D') == 500
assert roman_to_decimal('M') == 1000


assert roman_to_decimal('II') == 2
assert roman_to_decimal('III') == 3
assert roman_to_decimal('IV') == 4
assert roman_to_decimal('V') == 5
assert roman_to_decimal('VI') == 6
assert roman_to_decimal('VII') == 7
assert roman_to_decimal('VIII') == 8
assert roman_to_decimal('IX') == 9
assert roman_to_decimal('X') == 10
assert roman_to_decimal('XI') == 11
assert roman_to_decimal('XII') == 12
assert roman_to_decimal('XIII') == 13
assert roman_to_decimal('XIV') == 14
assert roman_to_decimal('XV') == 15
assert roman_to_decimal('XVI') == 16
assert roman_to_decimal('XVII') == 17
assert roman_to_decimal('XVIII') == 18
assert roman_to_decimal('XIX') == 19
assert roman_to_decimal('XX') == 20
