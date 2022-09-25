#Преобразуйте переменную age и foo в число
#age = "23"
#foo = "23abc"
#Преобразуйте переменную age в Boolean
#age = 123abc
#Преобразуйте переменную flag в Boolean
#flag = 1
#Преобразуйте значение  в Boolean
#str_one = "Privet"
#str_two = ""
#Преобразуйте значение 0 и 1  в Boolean

age = int("23")
print (age)

foo = str("23abc")
print (int(foo[:2]), " Не возможно преобразовать текст в число")

age1 = bool("123abc")
print (age1)

flag = bool(1)
print (flag)

str_one = bool("Privet")
print (str_one)

str_two = bool("")
print (str_two)

str_3 = bool(1)
print (str_3)

str_4 = bool(0)
print (str_4)

