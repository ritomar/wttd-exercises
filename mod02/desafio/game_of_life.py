# Conway escolheu suas regras cuidadosamente, após um longo período de experimentos,
# para satisfazer três critérios:
#
# Não deve haver nenhuma imagem inicial para a qual haja uma prova imediata ou trivial
# de que a população pode crescer sem limite.
#
# Deve haver imagens iniciais que aparentemente cresçam sem limite.
#
# Deve haver imagens iniciais simples que cresçam e mudem por um período de tempo
# considerável antes de chegar a um fim das possíveis formas:
#
# - Sumindo completamente (por superpopulação ou por ficarem muito distantes)
#
# - Estacionando em uma configuração estável que se mantem imutável para sempre, ou
#   entrando em uma fase de oscilação na qual são repetidos ciclos infinitos de dois
#   ou mais períodos.
#
# Em outras palavras, as regras deviam tornar o comportamento das populações ao mesmo
# tempo interessante e imprevisível.
#
# As regras são simples e elegantes:
#
# 1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
#
# 2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
#
# 3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
#
# 4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para
#    a próxima geração.
#
# É importante entender que todos os nascimentos e mortes ocorrem simultaneamente.
#
# Juntos eles constituem uma geração ou, como podemos chamá-los, um "instante" na história da vida completa da configuração inicial.


from random import randrange

LIVE = 1
DEAD = 0
TAB_LINES = 3
TAB_ROWS = 3
VIVOS = 4

def live(grid, cell):
    line, row = cell
    grid[line][row] = LIVE


def dead(grid, cell):
    line, row = cell
    grid[line][row] = DEAD


def print_grid(grid, with_neighbours=False):
    for line in grid:
        for item in line:
            print('%4s' % item, end='')
        print('')

    print('\n')

    if with_neighbours:
        vizinhos = neighbours_(grid)
        print('vizinhos:')
        print_grid(vizinhos)


def is_valid_cell(cell):
    return cell[0] >= 0 and cell[1] >= 0 and cell[0] < TAB_LINES and cell[1] < TAB_ROWS

def count_neighbours(grid, cell):
    line, row = cell


    idx_nb_1 = (line - 1, row - 1)
    idx_nb_2 = (line - 1, row)
    idx_nb_3 = (line - 1, row + 1)
    idx_nb_4 = (line, row - 1)
    idx_nb_5 = (line, row + 1)
    idx_nb_6 = (line + 1, row - 1)
    idx_nb_7 = (line + 1, row)
    idx_nb_8 = (line + 1, row + 1)

    # Test edges
    idx_nb_1 = idx_nb_1 if is_valid_cell(idx_nb_1) else ()
    idx_nb_2 = idx_nb_2 if is_valid_cell(idx_nb_2) else ()
    idx_nb_3 = idx_nb_3 if is_valid_cell(idx_nb_3) else ()
    idx_nb_4 = idx_nb_4 if is_valid_cell(idx_nb_4) else ()
    idx_nb_5 = idx_nb_5 if is_valid_cell(idx_nb_5) else ()
    idx_nb_6 = idx_nb_6 if is_valid_cell(idx_nb_6) else ()
    idx_nb_7 = idx_nb_7 if is_valid_cell(idx_nb_7) else ()
    idx_nb_8 = idx_nb_8 if is_valid_cell(idx_nb_8) else ()

    sum_ = 0;
    if idx_nb_1:
        sum_ += grid[idx_nb_1[0]][idx_nb_1[1]]
    if idx_nb_2:
        sum_ += grid[idx_nb_2[0]][idx_nb_2[1]]
    if idx_nb_3:
        sum_ += grid[idx_nb_3[0]][idx_nb_3[1]]
    if idx_nb_4:
        sum_ += grid[idx_nb_4[0]][idx_nb_4[1]]
    if idx_nb_5:
        sum_ += grid[idx_nb_5[0]][idx_nb_5[1]]
    if idx_nb_6:
        sum_ += grid[idx_nb_6[0]][idx_nb_6[1]]
    if idx_nb_7:
        sum_ += grid[idx_nb_7[0]][idx_nb_7[1]]
    if idx_nb_8:
        sum_ += grid[idx_nb_8[0]][idx_nb_8[1]]

    return sum_


def neighbours_(game):
    # Cria grade para vizinhos
    vizinhos = []
    for i in range(len(game)):
        vizinhos.append([])
        for j in range(len(game[i])):
            vizinhos[i].append(game[i][j])

    # Calcula quantidade de vizinhos
    for i in range(TAB_LINES):
        for j in range(TAB_ROWS):
            vizinhos[i][j] = count_neighbours(game, (i, j))

    return vizinhos


def next_generation(grid):
    has_next = False
    for line in range(TAB_LINES):
        for row in range(TAB_ROWS):
            n = neighbours(grid, (line, row))
            # 1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
            if grid[line][row] == LIVE and n < 2:
                dead(grid, (line, row))
                has_next = True

            # 2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
            if grid[line][row] == LIVE and n > 3:
                dead(grid, (line, row))
                has_next = True

            # 3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
            if grid[line][row] == DEAD and n == 3:
                live(grid, (line, row))
                has_next = True

            # 4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para
            #    a próxima geração.
            if grid[line][row] == LIVE and (n == 3 or n == 3):
                live(grid, (line, row))
                has_next = True

    return has_next




def new_game(lines, rows, start):
    new_game = []

    for i in range(lines):
        line = []

        for l in range(rows):
            line.append(DEAD)

        new_game.append(line)

    box = []

    while len(box) < start:
        x, y = randrange(lines), randrange(rows)

        if (x, y) not in box:
            box.append((x, y))

    for i in box:
        live(new_game, i)


    return new_game


print('Starting...\n')
game = new_game(TAB_LINES, TAB_ROWS, VIVOS)
# game = [[0, 0, 1],
#         [0, 1, 0],
#         [1, 1, 0]]
print_grid(game, with_neighbours=True)


qtd = 1

while qtd < 100:
    continua = False
    neighbours = neighbours_(game)
    for i in range(TAB_LINES):
        for j in range(TAB_ROWS):
            # print('(%d,%d)' % (i, j), game[i][j], 'v:', neighbours[i][j])
            if game[i][j] == 1 and neighbours[i][j] < 2:
                # print ('vivo | v < 2 --> morto')
                game[i][j] = 0
                continua = True
            elif game[i][j] == 1 and neighbours[i][j] > 3:
                # print ('vivo | v > 3 --> morto')
                # print (i, j)
                game[i][j] = 0
                continua = True
            elif (game[i][j] == 0) and neighbours[i][j] == 3:
                # print ('morto | v == 3 --> vivo')
                game[i][j] = 1
                continua = True

    print('geração %d:' % qtd)
    print_grid(game, with_neighbours=True)

    qtd += 1
    if not continua: break

