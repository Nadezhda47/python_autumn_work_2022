#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

matrix = [[1, 2, 3], [4, 5, 6]]

def msum(mtr):
    summ_matr = sum([x for mtr in mtr for x in mtr])
    print("Сумма элементов матрицы ", mtr, " равна ", summ_matr)

msum(matrix)