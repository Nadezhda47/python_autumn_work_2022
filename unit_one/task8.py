#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
#A = 1010
#B = 3
#C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
#A = 2
#B = 10
#C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C =
a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
c = float(input("Введите третье число "))
if a < b <= c:
    print (c)
    print (b)
    print (a)
elif a < b > c >= a:
    print (b)
    print (c)
    print (a)
elif c <= a <= b >= c:
    print(b)
    print(a)
    print(c)
elif c < a < b >= c:
    print(b)
    print(a)
    print(c)
elif a >= b < c > a:
    print(c)
    print(a)
    print(b)
elif a >= b >= c:
    print(a)
    print(b)
    print(c)
elif a >= b < c <= a:
    print(a)
    print(c)
    print(b)
else:
    print("Пиши дальше")