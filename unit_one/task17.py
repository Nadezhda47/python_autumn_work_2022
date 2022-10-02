#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

check_count = {}

prod_value = (1, 3, 2, 0)
prod_key = prices.keys()

check_count = dict(zip (prod_key, prod_value))


def compute_bill (food):
    Summ = 0
    for key in food:
        Summ += prices[key]
    return (Summ)

compute_bill = compute_bill(check_count)
print("Сумма товаров", compute_bill)