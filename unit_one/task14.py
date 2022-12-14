#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального растояния т.к элемент в массиве один.
mass = [1,2,17,54,30,89,2,1,21,6,2,1,17]

x_index = [] # список для хранения индексов
i = 0 #переменная для счетчика
k = 0 #счетчик вхождений
n = "" #номер индекса

for k in range(len(mass)):
    if mass[:k].count(mass[k]) < 1:
        if mass.count(mass[k]) > 1:
            x = [i for i, ltr in enumerate(mass) if ltr == mass[k]]
            st = [j-i for i, j in zip(x[:-1], x[1:])]
            r = min (st)
            ind_r = st.index(r)
            min_1 = x[ind_r+1]
            min_2 = x[ind_r]
            print("Для числа ", mass[k], " минимальное растояние в массиве по индексам: ", min_1, "и", min_2)
            k = k + 1
        else:
            print("Для числа", mass[k], "нет минимального растояния т.к элемент в массиве один.")
            k = k + 1
    else:
        k = k + 1