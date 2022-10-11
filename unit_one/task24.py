#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

"""Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!"""""
i = 0
r = 0
text_2 = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
numb_lett = """"""


text = input("Введите числа")
x = text.split(" ")
for i in range(len(x)):
    if x[i].isdigit():
        r = text_2[int(x[i])]
        numb_lett += r
        i += 1
    else:
        numb_lett += x[i]
        i += 1
print(numb_lett)