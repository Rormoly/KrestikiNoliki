import time
import random
import os

matrix = [[" ", 0, 1, 2],
          [0, "-", "-", "-"],
          [1, "-", "-", "-"],
          [2, "-", "-", "-"]]

# Очистка вывода
def clear():
    os.system("cls")
    print_matrix()

# Функция печатия поля (вывод игровой матрицы, если простым языком)
def print_matrix():
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

# Проверка на корректность ввода
def is_valid_input(user_input):
    if len(user_input) != 2 or not user_input.isdigit():
        return False
    x, y = map(int, user_input)
    return 0 <= x <= 2 and 0 <= y <= 2 and matrix[x + 1][y + 1] == "-"

# Проверка на завершённость игры
def check_winner(symbol):
    # Проверка строк, столбцов и диагоналей
    for i in range(1, 4):
        if all(matrix[i][j] == symbol for j in range(1, 4)) or \
           all(matrix[j][i] == symbol for j in range(1, 4)):
            return True
    if matrix[1][1] == matrix[2][2] == matrix[3][3] == symbol or \
       matrix[1][3] == matrix[2][2] == matrix[3][1] == symbol:
        return True
    return False

# Ход компьютера
def computer_move(symbol):
    time.sleep(2)
    oponent_symbol = "X" if symbol == "O" else "O"
    possible_moves = [(x, y) for x in range(1, 4) for y in range(1, 4) if matrix[x][y] == "-"]
    # Проверка хода на свою победу
    for x, y in possible_moves:
        matrix[x][y] = symbol
        if check_winner(symbol):
            return
        matrix[x][y] = "-"
    # Проверка хода на победу пользователя
    for x, y in possible_moves:
        matrix[x][y] = oponent_symbol
        if check_winner(oponent_symbol):
            matrix[x][y] = symbol
            return
        matrix[x][y] = "-"
    # Случайный ход, если нет выигрышного
    x, y = random.choice(possible_moves)
    matrix[x][y] = symbol


def main():
    os.system("cls")
    user_symbol = input("Выберите, за кого будете играть (X или O): ").upper()
    while user_symbol not in ("X", "O"):
        os.system("cls")
        print("Некорректный ввод. Выберите X или O.")
        user_symbol = input("Выберите, за кого будете играть (X или O): ").upper()

    computer_symbol = "O" if user_symbol == "X" else "X"
    clear()

    for turn in range(9):
        if (turn % 2 == 0 and user_symbol == "X") or (turn % 2 == 1 and user_symbol == "O"):
            user_input = input("Введите координаты (например, 00): ")
            while not is_valid_input(user_input):
                clear()
                print("Некорректный ввод. Попробуйте ещё раз.")
                user_input = input("Введите координаты (например, 00): ")
            x, y = map(int, user_input)
            matrix[x + 1][y + 1] = user_symbol
        else:
            print("Ход компьютера...")
            computer_move(computer_symbol)

        clear()

        if check_winner(user_symbol):
            print("Поздравляем, вы выиграли!")
            return
        if check_winner(computer_symbol):
            print("Компьютер победил!")
            return

    print("Ничья!")

if __name__ == "__main__":
    main()
