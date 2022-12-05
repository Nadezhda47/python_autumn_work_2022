import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="dip",
    user="postgres",
    password="1234")
cur = conn.cursor()

# creating table
sql = '''CREATE TABLE product(
      id  SERIAL NOT NULL,
      product_shop varchar(40) not null,
      product_group varchar(100) not null,
      product_name varchar(100) not null,
      product_price int not null,
      product_url varchar(120) not null,
      product_data date not null);'''

cur.execute(sql)

# Commit your changes in the database
conn.commit()

insert_query = f"""INSERT INTO product
            (id, product_shop, product_group, product_name, product_price, product_url, product_data)
            VALUES
            (1 ,'Наименование магазина','Наименование группы', 'Наименование продукта', 1, 'ссылка', '04-12-2022');"""

cur.execute(insert_query)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

print("База данных успешно создана")