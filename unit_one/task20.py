#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

f = open("import_this.txt", mode='w+', encoding="utf-8")
lines = ["Beautiful is better than ugly.\n",
"Explicit is better than implicit.\n",
"Simple is better than complex.\n",
"Complex is better than complicated.\n"]#37
f.writelines(lines)
f.seek(0)

rever = f.readlines()
rever.reverse()
print(''.join(rever))
f.close()





