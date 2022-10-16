
#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
#Пример:
#render, 10,  12.05.2022 12:00
#show,    5,  12.05.2022 12:02
#render, 15,  12.05.2022 12:07
#Декоратор должен применяться для различных функций с переменным числом аргументов.
#Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import datetime, logging


mass = range(111111)
count = 0
def decorator_first(func):
    def wrapper(mass):
        global count
        count += 1
        func(mass)
        logging.basicConfig(
            filename = "debug.log",
            level=logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filemode='w',
        )
    return wrapper

def render(mass):
    a = sorted(mass)
    return a
def show (mass):
    print(mass)


wrap_func = decorator_first(render)
wrap_func(mass)

