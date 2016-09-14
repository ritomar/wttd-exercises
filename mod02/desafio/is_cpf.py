def is_cpf(cpf):
    exceptions = (
        '000000000', '111111111', '222222222', '333333333', '444444444',
        '555555555', '666666666', '777777777', '888888888', '999999999',
        '123456789',
    )

    test = cpf.replace('.', '').replace('-', '')[:-2]

    if (len(test) != 9) or (not test.isdigit()) or test in exceptions:
        print('CPF:', cpf, 'bad formated or an exception for valid CPF')
        return False

    soma, k = 0, 2
    for c in test[::-1]:
        soma += (int(c) * k)
        k += 1

    dv = 0 if (soma % 11) < 2 else 11 - (soma % 11)

    test += str(dv)

    soma, k = 0, 2
    for c in test[::-1]:
        soma += (int(c) * k)
        k += 1

    dv = 0 if (soma % 11) < 2 else 11 - (soma % 11)

    test += str(dv)

    print('CPF:', cpf, 'Expected:', cpf[-2:], 'Calculated:', test[-2:])
    return cpf.replace('.', '').replace('-', '') == test


VALID = True
INVALID = not VALID

cpfs_for_tests = (
    ('111.444.777-35', VALID),
    ('954.781.227-00', VALID),
    ('163.676.382-02', VALID),
    ('287.168.398-03', VALID),
    ('288.353.438-10', VALID),
    ('710.463.972-14', VALID),
    ('138.578.815-18', VALID),
    ('891.118.785-25', VALID),
    ('781.747.606-36', VALID),
    ('884.411.937-46', VALID),
    ('685.551.804-49', VALID),
    ('845.916.632-56', VALID),
    ('389.178.972-66', VALID),
    ('696.726.344-71', VALID),
    ('840.984.481-81', VALID),
    ('782.542.731-97', VALID),

    ('011.444.777-35', INVALID),
    ('914.781.227-00', INVALID),
    ('162.676.382-02', INVALID),
    ('287.368.398-03', INVALID),
    ('288.343.438-10', INVALID),
    ('710.465.972-14', INVALID),
    ('138.578.615-18', INVALID),
    ('891.118.775-25', INVALID),
    ('781.747.608-36', INVALID),
    ('884.411.937-96', INVALID),
    ('685.551.804-40', INVALID),
    ('845.916.632-16', INVALID),
    ('389.178.973-66', INVALID),
    ('696.726.324-71', INVALID),
    ('840.984.181-81', INVALID),
    ('782.540.731-97', INVALID),

    ('000.000.000-00', INVALID),
    ('111.111.111-11', INVALID),
    ('222.222.222-22', INVALID),
    ('333.333.333-33', INVALID),
    ('444.444.444-44', INVALID),
    ('555.555.555-55', INVALID),
    ('666.666.666-66', INVALID),
    ('777.777.777-77', INVALID),
    ('888.888.888-88', INVALID),
    ('999.999.999-99', INVALID),
    ('123.456.789-09', INVALID),
)


for cpf, expected in cpfs_for_tests:
    assert is_cpf(cpf) == expected
