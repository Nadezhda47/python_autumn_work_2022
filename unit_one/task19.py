#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm
#Каждое значение из списка должно находится на отдельной строке.
import csv

algoritm = ["C4.5","k - means","Метод опорных векторов","Apriori","EM","PageRank","AdaBoost","kNN","Наивный байесовский классификатор","CART"]
i = 0
y = []
y = list(range(1, 11))
l = list(zip(y, algoritm))
fp = open("algoritm.csv", mode='at', encoding="utf-8")
writer = csv.writer(fp, delimiter =' ',quotechar =',')
for i in range(len(l)):
 writer.writerow(l[i])
 i += 1

fp.close()
