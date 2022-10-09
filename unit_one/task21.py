# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

key_mass = []
k = 0 #Переменная для ключей
i = 1 #Переменная для перебора строк
template1 = """"""

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>
 </body>
</html>
"""


key_mass = list(page.keys())
print(key_mass)
print(template.count("?"))
template1 = template

for i in range(template.count("?")):
    template1 = template1.replace("?",key_mass[i], 1)
    print(template1)
    print(i)
    i += 1
    
f = open("index.html", mode='a', encoding="utf-8")
f.writelines(template1)
