maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [6, 4, 2]]
#Приветствие
print('Добро пожаловать в игру "Крестики - нолики" ')

#Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])
#Делаем ход
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind]  = symbol

#Получаем текущий результат
def get_result():
    win = " "
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Игрок"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Компьютер"
    return win

#Компьютер: поиск линии с нужным количеством X и O на победных линиях
def chek_line(sum_O, sum_X):

    step = " "

    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]

    return step

#Компьютер выбирает ход
def AI():

    step = " "

    step = chek_line(2, 0)

    if step == " ":
        step = chek_line(0, 2)

    if step == " ":
        step = chek_line(1, 0 )

    if step == " ":
        if maps[4] != "X" and maps[4] != "O":
            step = 5

    if step == " ":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step


#Главная программа:
game_over = False
player = True

while game_over == False:

    print_maps()

    if player == True:
        symbol = "X"
        step = int(input('Игрок делает свой ход: '))
    else:
        print('Компьютер делает ход: ')
        symbol = "O"
        step = AI()

    if step != " ":
        step_maps(step, symbol)
        win = get_result()
        if win != " ":
            game_over = True
        else:
            game_over = False

    else:
        print("Игра закончилась ничьей! ")
        game_over = True
        win = "Победила дружба"

    player = not(player)

#Игра окончена
print_maps()
print("Победил", win)














