# Создание игрового поля 3 х 3
playing_field = [["-" for _ in range(3)] for _ in range(3)]

# Функция для вывода игрового поля
def print_field():
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(playing_field[i])}")

# Проверка победы
def check_win(player):
    # Проверка строк
    for row in playing_field:
        if row.count(player) == 3:
            return True
    # Проверка столбцов
    for col in range(3):
        if all(playing_field[row][col] == player for row in range(3)):
            return True
    # Проверка диагоналей
    if all(playing_field[i][i] == player for i in range(3)):
        return True
    if all(playing_field[i][2 - i] == player for i in range(3)):
        return True
    return False

# Проверка ничьи
def check_draw():
    for row in playing_field:
        if "-" in row:
            return False
    return True

# Ход игрока с проверкой
def move(player):
    while True:
        try:
            coords = input(f"Ход игрока {player}. Введите координаты (строка и столбец через пробел): ")
            x, y = map(int, coords.split())
            if x not in range(3) or y not in range(3):
                print("Таких координат не существует. Попробуйте еще раз.")
                continue
            if playing_field[x][y] != "-":
                print("Клетка занята. Попробуйте еще раз.")
                continue
            playing_field[x][y] = player
            break
        except ValueError:
            print("Неправильный ввод. Введите два числа через пробел.")

# Основной цикл игры
def game():
    print("Добро пожаловать в Крестики-Нолики! Да победит сильнейший!")
    current_player = "X"
    while True:
        print_field()
        move(current_player)
        if check_win(current_player):
            print_field()
            print(f"Игрок {current_player} выиграл!")
            break
        if check_draw():
            print_field()
            print("НИЧЬЯ!")
            break
        current_player = "O" if current_player == "X" else "X"

game()