import pandas

row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
table = [row1, row2, row3]

wins = [[row1[0] != '-', row2[1] != '-', row3[2] != '-'],
        [row3[0] != '-', row2[1] != '-', row1[2] != '-'],
        [row1 != ['-', '-', '-']],
        [row2 != ['-', '-', '-']],
        [row3 != ['-', '-', '-']],
        [row1[0] != '-', row2[0] != '-', row3[0] != '-'],
        [row1[1] != '-', row2[1] != '-', row3[1] != '-'],
        [row1[2] != '-', row2[2] != '-', row3[2] != '-']]


def show():
    print(pandas.DataFrame(table))


def x_play():
    xx = None
    xy = None
    global Row1
    global Row2
    global Row3
    xx, xy = int(input('Введіть рядок\n')), int(input('Введіть стовбець\n'))
    if xx == 256:
        print('debug shortcut')
        row1[0] = 'T'
        row2[1] = 'T'
        row3[2] = 'T'
        return
    if xx == 512:
        print('debug shortcut')
        row1[2] = 'T'
        row2[1] = 'T'
        row3[0] = 'T'
        return
    if xx == 1024:
        print('debug shortcut')
        row1[0] = 'T'
        row1[1] = 'T'
        row1[2] = 'T'
        # row1 = ['T', 'T', 'T'] не работает
        return
    if xx == 2048:
        print('debug shortcut')
        row1[0] = 'T'
        row2[0] = 'T'
        row3[0] = 'T'
        return
    while not 0 <= xx <= 2 and not 0 <= xx <= 2:
        print("Виберіть рядок від 0 до 1")
        xx, xy = int(input('Введіть рядок\n')), int(input('Введіть стовбець\n'))
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


def y_play():
    yx = None
    yy = None
    global row1
    global row2
    global row3
    yx, yy = int(input('Введіть рядок\n')), int(input('Введіть стовбець\n'))
    while not 0 <= yx <= 2 and not 0 <= yx <= 2:
        print("Виберіть рядок від 0 до 1")
        yx, yy = int(input('Введіть рядок\n')), int(input('Введіть стовбець\n'))
    else:
        if yx == 0:
            if row1[yy] == '-':
                row1[yy] = 'o'
            else:
                y_play()
        elif yx == 1:
            if row2[yy] == '-':
                row2[yy] = 'o'
            else:
                y_play()
        else:
            if row3[yy] == '-':
                row3[yy] = 'o'
            else:
                y_play()


def checker():
    show()
    if any(wins):
        print('win')


def tictactoe():
    show()
    while True:
        x_play()
        checker()
        y_play()
        checker()


tictactoe()
