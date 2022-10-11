#todo: Взлом шифра

text = """grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."""

text_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]
i = 0
k = 1
r = 0
uncode = """"""

while k <= 26:
    for i in range(len(text)):
        if text[i] not in text_2:
            uncode += text[i]
            i += 1
        else:
            r = text_2.index(text[i])
            uncode += text_2[r-k]
            i += 1
    print(uncode)
    k += 1
    uncode = """"""

while k <= 26:
    for i in range(len(text)):
        if text[i] not in text_2:
            uncode += text[i]
            i += 1
        else:
            r = text_2.index(text[i])
            uncode += text_2[r-k]
            i += 1
    print(uncode)
    k += 1
    uncode = """"""

print("Взломанный шифр в 6 строке")