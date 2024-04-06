"""Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
единицу измерения (штуки, килограммы, литры), количество, стоимость."""


import sqlite3

data = [('Рычков', 'Данил', 'Викторович', 'Вода', 'литры', '19', '230'),
        ('Мансуров', 'Александр', 'Максимович', 'Соль', 'килограммы', '139', '32'),
        ('Меркулов', 'Никита', 'Владимирович', 'Доширак', 'штуки', '1', '20'),
        ('Коренной', 'Никита', 'Владимирович', 'Карась сушенный', 'штуки', '5', '299'),
        ('Гречанов', 'Кирилл', 'Демьянович', 'Сдобный пирожок с сыром', 'штуки', '1', '25'),
        ('Рычков', 'Иван', 'Викторович', 'Сухарики "Хрустим"', 'штуки', '1', '12'),
        ('Кресиченко', 'Данил', 'Валерьевич', 'Молоко', 'литры', '1', '69'),
        ('Ковалев', 'Олег', 'Олегович', 'Стиральный порошок', 'килограммы', '5', '490'),
        ('Щербаков', 'Виталий', 'Олегович', 'Пельмени', 'килограммы', '4', '499'),
        ('Монакова', 'Ольга', 'Петровна', 'Мороженое', 'штуки', '1', '23')]


with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sales(
    LastName TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    Patronymic TEXT,
    Product TEXT NOT NULL,
    UnitOFMeasure TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    Price INTEGER NOT NULL 
    )""")

with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?,?)", data)


with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sales")
    print('\n\nЗАПРОС К ДАННЫМ--------')
    for result in cursor.fetchall():
        print(result)

with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sales WHERE UnitOFMeasure='килограммы'")
    print('\n\nЗАПРОС К ДАННЫМ--------')
    for result in cursor.fetchall():
        print(result)

with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sales WHERE UnitOFMeasure='литры' AND Quantity >= 1")
    print('\n\nЗАПРОС К ДАННЫМ--------')
    for result in cursor.fetchall():
        print(result)



with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("UPDATE sales SET Quantity=2 WHERE LastName='Монакова'")
    cursor.execute("UPDATE sales SET PRICE=24 WHERE LastName='Рычков' AND FirstName='Иван'")


with sqlite3.connect('WebShop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("DELETE FROM sales WHERE Product='Карась сушенный'")
    cursor.execute("DELETE FROM sales WHERE LastName='Рычков' AND Product='Вода'")
    cursor.execute("DELETE FROM sales WHERE LastName='Мансуров'")
    print('\n\nУДАЛЕНИЕ ДАННЫХ--------')
    cursor.execute("SELECT * FROM sales")
    for result in cursor.fetchall():
        print(result)
