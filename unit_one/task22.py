# todo: Шифр Цезаря
#Задача.
#Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
#циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

text = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
        "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й",
        "К",  "Л",  "М",  "Н",  "О",  "П",  "Р",  "С",  "Т",  "У",  "Ф",  "Х",  "Ц",  "Ч",  "Ш",  "Щ",  "Ъ",  "Ы",  "Ь",
        "Э",  "Ю",  "Я")

f = open("message.txt", mode='r+t', encoding="utf-8")
p = """"""
s = """"""
i = 0
k = 1
j = 0

for line in f:
    for i in range(len(line)):
        if line[i] not in text:
            p += line[i]

        else:
            j = text.index(line[i])
            p += text[j+k]
        i += 1
    k += 1
print(p)
