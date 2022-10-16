# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.

# Пример:
from random import randint as rdi
game_field = []
i = 0
k = 10
gen_x = 0
gen_y = 0


#while gen_x in range(len(game_field)):
#    otg.append("X")
#    gen_x = gen_x + 1
def matrix():
    global game_field
    n = int(input("Введите количество ячеек по горизонтали "))
    m = int(input("Введите количество ячеек по вертикали "))
    game_field = [[rdi(0, 1) for _ in range(n)] for _ in range(m)]


def game():
    global k
    matrix()
    print(game_field)
    while k > 0:
        pos_horizont = int(input("Введите номер ячейки по горизонтали"))
        pos_vertical = int(input("Введите номер ячейки по вертикали"))

        if game_field[pos_horizont][pos_vertical] == 1:
            print("Есть попадание!")

        else:
            print("Мимо, попробуйте еще раз")
            k = k - 1


game()
