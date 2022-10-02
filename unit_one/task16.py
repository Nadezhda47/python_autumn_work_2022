#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.


words = ["оператор", "конструкция", "объект"]
desc_ = [ "Это слово обозначает наименьшую автономную часть языка программирования", "следование, ветвление и цикл - это ...", "Некоторая сущность в цифровом пространстве, обладающая определённым состоянием и поведением, имеющая определенные свойства и операции над ними" ]

import random
att = random.randint(0,2)
otg = []
gen_x = 0
i = 0
slovo = words[att]

while gen_x in range(len(slovo)):
    otg.append("X")
    gen_x = gen_x + 1

time = 10
x = 0
k = 0

def quantity_2 (text, text2):
    p = []
    fp = 0
    p = [i for i, ltr in enumerate(text) if ltr == text[text.index(x)]]
    while fp < len(p):
        text2[p[fp]] = x
        fp = fp + 1
    return text2

print("Внимание, вопрос!")
print (desc_[att])
print (otg)
print ("В этом слове ", len(otg), " букв")




while otg.count("X") > 0 and time > 0:
    if otg.count("X") > 0:

        x = str(input("Назовите букву "))
        if slovo.count(x) > 1:
            quantity = quantity_2(slovo, otg)
            print("Есть такая буква!")
            print(quantity)
            print("Количество оставшихся попыток: ", time)
        elif slovo.count(x) == 1:
            print("Есть такая буква!")
            otg[slovo.index(x)] = x
            print(otg)
            print("Количество оставшихся попыток: ", time)
        else:
            print("В этом слове нет такой буквы")
            time = time - 1
            print("Количество оставшихся попыток: ", time)
    else:
        print("Игра окончена!")

else:
    print("Игра окончена!")
