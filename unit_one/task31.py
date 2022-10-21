
#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
#Пример:
#render, 10,  12.05.2022 12:00
#show,    5,  12.05.2022 12:02
#render, 15,  12.05.2022 12:07
#Декоратор должен применяться для различных функций с переменным числом аргументов.
#Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import logging

mass = range(111111)
count = 0
count2 = 0
def decorator_first(func):
    global count

    def wrapper(mass):
        global count
        count += 1
        func(mass)
        logging.basicConfig(
            filename = "debug.log",
            level=logging.DEBUG,
            format='%(message)s, %(asctime)s ',
            filemode='at',
        )
        logging.debug(f'{func.__name__} {count}')

    return wrapper


@ decorator_first
def render(mass):
    a = sorted(mass)
    return a
@ decorator_first
def show (mass):
    print(mass)

render (mass)
render (mass)
render (mass)
