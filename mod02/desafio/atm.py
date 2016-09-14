# Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.
#
# - Os requisitos básicos são os seguintes:
# - Entregar o menor número de notas;
# - É possível sacar o valor solicitado com as notas disponíveis;
# - Saldo do cliente infinito;
# - Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
# - Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
#
# Exemplos:
# Valor do Saque: R$ 30,00 – Resultado Esperado:
# Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
#
# Valor do Saque: R$ 80,00 – Resultado Esperado:
# Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.

SUCCESS = 0
ONE_HUNDRED_BILLS = 1
FIFTY_BILLS = 2
TWENTY_BILLS = 3
TEN_BILLS = 4

def atm_message(cash_dispenser_tuple):
    if cash_dispenser_tuple[SUCCESS]:
        plural = ('nota', 'notas')
        message = []
        if cash_dispenser_tuple[ONE_HUNDRED_BILLS] > 0:
            message.append(
                str(cash_dispenser_tuple[ONE_HUNDRED_BILLS]) + ' ' +
                (plural[0] if cash_dispenser_tuple[ONE_HUNDRED_BILLS] == 1 else plural[1]) +
                ' R$ 100,00'
            )
        if cash_dispenser_tuple[FIFTY_BILLS] > 0:
            message.append(
                str(cash_dispenser_tuple[FIFTY_BILLS]) + ' ' +
                (plural[0] if cash_dispenser_tuple[FIFTY_BILLS] == 1 else plural[1]) +
                ' R$ 50,00'
            )

        if cash_dispenser_tuple[TWENTY_BILLS] > 0:
            message.append(
                str(cash_dispenser_tuple[TWENTY_BILLS]) + ' ' +
                (plural[0] if cash_dispenser_tuple[TWENTY_BILLS] == 1 else plural[1]) +
                ' R$ 20,00'
            )

        if cash_dispenser_tuple[TEN_BILLS] > 0:
            message.append(
                str(cash_dispenser_tuple[TEN_BILLS]) + ' ' +
                (plural[0] if cash_dispenser_tuple[TEN_BILLS] == 1 else plural[1]) +
                ' R$ 10,00'
            )

            print(' '.join(message))
    else:
        return 'Não foi possível realizar a operação'


def atm(value):
    if value == 0 or value % 10 != 0:
        return (False, 0, 0, 0, 0)
    one_hundred_bills = value // 100
    value %=  100
    fifty_bills = value // 50
    value %= 50
    twenty_bills = value // 20
    value %= 20
    ten_bills = value // 10

    return (True, one_hundred_bills, fifty_bills, twenty_bills, ten_bills)

atm_message(atm(380))

assert atm(0) == (False, 0, 0, 0, 0)
assert atm(10) == (True, 0, 0, 0, 1)
assert atm(20) == (True, 0, 0, 1, 0)
assert atm(30) == (True, 0, 0, 1, 1)
assert atm(50) == (True, 0, 1, 0, 0)
assert atm(60) == (True, 0, 1, 0, 1)
assert atm(70) == (True, 0, 1, 1, 0)
assert atm(80) == (True, 0, 1, 1, 1)
assert atm(100) == (True, 1, 0, 0, 0)
assert atm(110) == (True, 1, 0, 0, 1)
assert atm(120) == (True, 1, 0, 1, 0)
assert atm(130) == (True, 1, 0, 1, 1)
assert atm(150) == (True, 1, 1, 0, 0)
assert atm(160) == (True, 1, 1, 0, 1)
assert atm(170) == (True, 1, 1, 1, 0)
assert atm(180) == (True, 1, 1, 1, 1)
