#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.
#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni

i = 0
numb_lett = """"""
x = str(input("Введите текст"))
text = x.lower()
while (i < len(text)):
    if text[i].isalpha() and text[i] not in numb_lett:
        numb_lett += text[i]
        i = i + 1
    else:
        i = i + 1
print(numb_lett)
