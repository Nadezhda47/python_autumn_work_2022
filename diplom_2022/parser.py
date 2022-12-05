import requests
from bs4 import BeautifulSoup
from datetime import datetime
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="dip",
    user="postgres",
    password="1234")
cur = conn.cursor()


def get_first_parth():
    """
    Функция для парсинга сайта 2MOOD
    """

    x = 1

    for x in range(25):
        url = f"https://www.2moodstore.com/collection/all?page={x}"
        x += 1

        max_id = cur.execute(f"""SELECT MAX(id) FROM product WHERE id is not null""")
        i = cur.fetchall()[0][0]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/106.0.0.0 YaBrowser/22.11.0.2500 Yowser/2.5 Safari/537.36"}
        # Создаем словарь заоловков

        r = requests.get(url=url, headers=headers)
        # GET запрос

        soup = BeautifulSoup(r.text, "html.parser")  # html.parser - это парсер для нашей функции
        product_cards = soup.find_all("a", class_="site-prod-name")

        for product in product_cards:
            i += 1

            product_name = product.find("p", class_="h6 name_wrapper").text.strip()
            product_group = product_name.split(" ")[0]
            product_url = f'https://www.2moodstore.com/{product.get("href")}'
            product_price = int(product.find("span", class_="money").text.split(" ")[0].replace(" ", ""))
            product_shop = "2MOOD"
            product_data_now = datetime.today()
            product_data = datetime.strftime(product_data_now, "%Y-%m-%d")

            insert_query = f"""INSERT INTO product
            (id, product_shop, product_group, product_name, product_price, product_url, product_data)
            VALUES('{i}', '{product_shop}', '{product_group}', '{product_name}', '{product_price}', '{product_url}', 
            '{product_data}');"""
            cur.execute(insert_query)

        # Commit your changes in the database
        conn.commit()


def main():
    # Добавляем функцию main для запуска функции get_first_parth

    get_first_parth()

    # Closing the connection
    conn.close()

    print("Данные успешно записаны")


if __name__ == '__main__':
    main()
