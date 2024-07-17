#Rahimberdiyev Lochinbek
# 1- masala 1.	Postgresql bazaga python yordamida ulaning .
# Product nomli jadval yarating  (id,name,price, color,image) .

import psycopg2
from psycopg2 import sql

DB_NAME = "Product"
DB_USER = "postgres"
DB_PASSWORD = "davon"
DB_HOST = "localhost"
DB_PORT = " 5432"



#2- masala.	Insert_product , select_all_products ,
# update_product,delete_product nomli funksiyalar yarating.

def create_connection():
    return psycopg2.connect(
        dbname="Product",
        user="postgres",
        password= "davon",
        host="localhost",
        port="5432"
    )

def create_product_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Product (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            color VARCHAR(50),
            image VARCHAR(255)
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'Product' created successfully")
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)

def insert_product(name, price, color, image):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO Product (name, price, color, image)
         VALUES (iphone_16, 2000, blue_titanium, img.phn) 
         RETURNING id;
        '''
        cursor.execute(insert_query, (name, price, color, image))
        connection.commit()
        product_id = cursor.fetchone()[0]
        print(f"Product inserted successfully with id {product_id}")
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting product", error)

def select_all_products():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        select_query = 'SELECT * FROM Product;'
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while selecting products", error)

def update_product(product_id, name=None, price=None, color=None, image=None):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        update_query = 'UPDATE Product SET '
        params = []
        if name:
            update_query += 'name = iphone_16 ,'
            params.append(name)
        if price:
            update_query += 'price = 2000 ,'
            params.append(price)
        if color:
            update_query += 'color = blue_titanium, '
            params.append(color)
        if image:
            update_query += 'image = img.phn '
            params.append(image)
        update_query = update_query.rstrip(', ')
        update_query += ' WHERE id = 1'
        params.append(product_id)
        cursor.execute(update_query, tuple(params))
        connection.commit()
        print(f"Product with id {product_id} updated successfully")
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while updating product", error)

def delete_product(product_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        delete_query = 'DELETE FROM Product WHERE id = %s'
        cursor.execute(delete_query, (product_id,))
        connection.commit()
        print(f"Product with id {product_id} deleted successfully")
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while deleting product", error)

# Example usage
create_product_table()
insert_product('Ball', 10.99, 'Red', 'image1.jpg')
insert_product('Cap', 15.49, 'Blue', 'image2.jpg')
select_all_products()
update_product(1, name='NewProduct', price=12.99)
select_all_products()
delete_product(1)
select_all_products()


# 5-masala .Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.




class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        try:
            connection = create_connection()
            cursor = connection.cursor()
            insert_query = '''
            INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s) RETURNING id;
            '''
            cursor.execute(insert_query, (self.name, self.price, self.color, self.image))
            connection.commit()
            product_id = cursor.fetchone()[0]
            print(f"Product saved successfully with id {product_id}")
            cursor.close()
            connection.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while saving product", error)

# Example usage
create_product_table()

product1 = Product('Brocli', 23.99, 'green', 'image.3.jpg')
product1.save()

product2 = Product('T-shirt', 16.49, 'white', 'image4.jpg')
product2.save()





# 3-masala 3.	Alphabet nomli class yozing .
# class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator).
# obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin

class Alphabet:
    def __iter__(self):
        self.current = 0
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return self

    def __next__(self):
        if self.current < len(self.letters):
            result = self.letters[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration
import time

def print_numbers(start, end):
    for num in range(start, end + 1):
        print(num)
        time.sleep(1)

def print_letters():
    letters = 'ABCDE'
    for letter in letters:
        print(letter)
        time.sleep(1)
import threading

# Define the Alphabet class
class Alphabet:
    def __iter__(self):
        self.current = 0
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return self

    def __next__(self):
        if self.current < len(self.letters):
            result = self.letters[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

# 4.	print_numbers va print_leters nomli funksiyalar yarating.
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa
# ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta thread yarating.
# Ekranga parallel ravishda itemlar chiqsin.
def print_numbers(start, end):
    for num in range(start, end + 1):
        print(num)
        time.sleep(1)

# Define the print_letters function
def print_letters():
    letters = 'ABCDE'
    for letter in letters:
        print(letter)
        time.sleep(1)

# Create two threads to run the functions in parallel
number_thread = threading.Thread(target=print_numbers, args=(1, 5))
letter_thread = threading.Thread(target=print_letters)

# Start the threads
number_thread.start()
letter_thread.start()

# Wait for both threads to finish
number_thread.join()
letter_thread.join()

#6- masala 6.	DbConnect nomli ContextManager yarating.
# Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)


import psycopg2

class DbConnect:
    def __init__(self, dbname, user, password, host, port='5432'):

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()

dbname = 'Product1'
user = 'postgres'
password = 'davon'
host = 'localhost'

with DbConnect(dbname, user, password, host) as (conn, cur):
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(f'Database version: {db_version[0]}')


    cur.execute('''
        CREATE TABLE IF NOT EXISTS Product1 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC NOT NULL,
            color VARCHAR(50),
            image VARCHAR(255)
        )
    ''')
    conn.commit()


    cur.execute('''
        INSERT INTO Product1 (name, price, color, image)
        VALUES (%s, %s, %s, %s)
    ''', ('Sample Product', 19.99, 'Red', 'image_url'))
    conn.commit()


    cur.execute('SELECT * FROM Product')
    products = cur.fetchall()
    for product in products:
        print(product)
 # 7- masala https://dummyjson.com/products/ urlga so’rov yuborib ,
# kelgan ma’lumotlarni Product nomli tabelga saqlang

import requests
import psycopg2
from contextlib import contextmanager
dbname = 'Product1'
user = 'postgres'
password = 'davon'
host = 'localhost'


@contextmanager
def db_connect():
    conn = psycopg2.connect(

    )
    cur = conn.cursor()
    try:
        yield conn, cur
    finally:
        cur.close()
        conn.close()



def create_product_table():
    with db_connect() as (conn, cur):
        cur.execute('''
             CREATE TABLE IF NOT EXISTS Product (
                 id SERIAL PRIMARY KEY,
                 name VARCHAR(100) NOT NULL,
                 price NUMERIC NOT NULL,
                 color VARCHAR(50),
                 image VARCHAR(255)
             )
         ''')
        conn.commit()


# Fetch Products Data from URL
def fetch_products():
    response = requests.get('https://dummyjson.com/products/')
    if response.status_code == 200:
        return response.json()['products']
    else:
        print("Failed to fetch data")
        return []


# Insert Products into Database
def insert_products(products):
    with db_connect() as (conn, cur):
        for product in products:
            cur.execute('''
                 INSERT INTO Product (name, price, color, image)
                 VALUES (%s, %s, %s, %s)
             ''', (product['title'], product['price'], product.get('color', 'N/A'), product['thumbnail']))
        conn.commit()



if __name__ == '__main__':
    create_product_table()
    products = fetch_products()
    if products:
        insert_products(products)
    else:
        print("No products to insert")
