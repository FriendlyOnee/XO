import pandas

row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
table = [row1, row2, row3]


def show():
    print(pandas.DataFrame(table))


def x_play():
    print("Играет крестик")
    xx = None
    xy = None
    global Row1
    global Row2
    global Row3
    xx, xy = int(input('Введите строчку\n')), int(input('Введите столбик\n'))
    if xx == 256:
        print('debug shortcut')
        row1[0] = 'x'
        row2[1] = 'x'
        row3[2] = 'x'
        return
    elif xx == 512:
        print('debug shortcut')
        row1[2] = 'x'
        row2[1] = 'x'
        row3[0] = 'x'
        return
    elif xx == 1024:
        print('debug shortcut')
        row1[0] = 'x'
        row1[1] = 'x'
        row1[2] = 'x'
        # row1 = ['T', 'T', 'T'] не работает
        return
    elif xx == 2048:
        print('debug shortcut')
        row1[0] = 'x'
        row2[0] = 'x'
        row3[0] = 'x'
        return
    while not 0 <= xx <= 2 and not 0 <= xy <= 2:
        print("Выберите правильные координаты")
        xx, xy = int(input('Введите строчку\n')), int(input('Введите столбик\n'))
    else:
        if xx == 0:
            if row1[xy] == '-':
                row1[xy] = 'x'
            else:
                x_play()
        elif xx == 1:
            if row2[xy] == '-':
                row2[xy] = 'x'
            else:
                x_play()
        else:
            if row3[xy] == '-':
                row3[xy] = 'x'
            else:
                x_play()
    show()


def o_play():
    print("Играет нолик")
    ox = None
    oy = None
    global row1
    global row2
    global row3
    ox, oy = int(input('Введите строчку\n')), int(input('Введите столбик\n'))
    while not 0 <= ox <= 2 and not 0 <= oy <= 2:
        print("Выберите правильные координаты")
        ox, oy = int(input('Введите строчку\n')), int(input('Введите столбик\n'))
    else:
        if ox == 0:
            if row1[oy] == '-':
                row1[oy] = 'o'
            else:
                o_play()
        elif ox == 1:
            if row2[oy] == '-':
                row2[oy] = 'o'
            else:
                o_play()
        else:
            if row3[oy] == '-':
                row3[oy] = 'o'
            else:
                o_play()
    show()


def wincheck(table):
    for x in range(0, len(table)):
        if len([y for y in table[x] if y == "x"]) == len(table):
            print("Выйграл крестик")
            return True
        elif len([y for y in table[x] if y == "o"]) == len(table):
            print("Выйграл нолик")
            return True
    for x in range(0, len(table)):
        if len([y for y in table if y[x] == "x"]) == len(table):
            print("Выйграл крестик")
            return True
        elif len([y for y in table if y[x] == "o"]) == len(table):
            print("Выйграл Нолик")
            return True
    if len([y for y in range(0, len(table)) if table[y][len(table) - 1 - y] == "x"]) == len(table) or len(
            [y for y in range(0, len(table)) if table[y][y] == "x"]) == len(table):
        print("Выйграл крестик")
        return True
    elif len([y for y in range(0, len(table)) if table[y][len(table) - 1 - y] == "o"]) == len(table) or len(
            [y for y in range(0, len(table)) if table[y][y] == "o"]) == len(table):
        print("Выйграл нолик")
        return True


show()
while True:
    x_play()
    if wincheck(table):
        break
    o_play()
    if wincheck(table):
        break
