#todo. Транспонирование матрицы, transpose(matrix)
# level:hight
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.

mass = [[1, 2, 3], [4, 5, 6]]

def transpose(x):
    trans_m = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    print(trans_m)

transpose(mass)

