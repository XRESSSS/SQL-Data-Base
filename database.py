import sqlite3
import hashlib
from pprint import pprint

def encript_password(value: str) -> str:
    hashed_value = hashlib.md5(value.encode()).hexdigest()
    print(hashed_value)
    return hashed_value


with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()
    connection.create_function('encode', 1, encript_password)
    cursor.execute("PRAGMA foreign_keys = ON")

    # values = ['M12v3', 250, 200, 2]
    # query = """
    #     INSERT INTO device(title, price, whole_price, category_id)
    #     VALUES(?,?,?,?)
    # """
    #
    # cursor.execute(query, values)

    query = """
        SELECT device.title, whole_price, device.id, name, category_id
    FROM device
            LEFT JOIN category
        ON device.category_id = category.id 
        WHERE title LIKE '%12% AND whole_price > 200      
    """

    # WHERE
    # price % 100 = 0

    result = cursor.execute(query)

    pprint(result.fetchall())


#     query = """
#         CREATE TABLE IF NOT EXISTS user(
#             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             name TEXT NOT NULL,
#             login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
#             password TEXT NOT NULL,
#             address TEXT
#         )
#     """
#     cursor.execute(query)
#
#     query = """
#         CREATE TABLE IF NOT EXISTS category(
#             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             name VARCHAR(16) NOT NULL,
#             description TEXT
#         );
#         CREATE TABLE IF NOT EXISTS device(
#             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             title TEXT NOT NULL UNIQUE,
#             whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
#             price DECIMAL(10, 2) CHECK (price >= whole_price),
#             category_id INTEGER,
#             FOREIGN KEY (category_id) REFERENCES category(id)
#         )
#     """
#     cursor.executescript(query)
#
#     name = 'Max'
#     password = '123456'
#     login = 'qwerty3'
#     values = [name, login, password]
#
#     query = """
#         INSERT INTO user(name, login, password)
#         VALUES (?, ?, encode(?))
#     """
#     cursor.execute(query, values)
#
#     values = (
#         ('1', '2132434', '3'),
#         ('1', '2132aadhgf434', '3'),
#         ('1', '213dsadsa2434', '3')
#     )
#
#     query = """
#         INSERT INTO user(name, login, password)
#         VALUES (?, ?, encode(?))
#     """
#     cursor.executemany(query, values)
#     READ
#     query = """
#         SELECT name, address
#         FROM user
#         WHERE id >= 3
#     """
#     query = """
#         SELECT name, address
#         FROM user
#         WHERE id > 3 AND address = 'Київ'
#     """
#     query = """
#         SELECT name, address
#         FROM user
#         WHERE id > 3 AND address LIKE '%Київ%'
#     """
#     query = """
#         SELECT name, address
#         FROM user
#         WHERE id BETWEEN 3 and 6
#     """
#     query = """
#         SELECT name, address
#         FROM user
#         WHERE id = 3 OR name = '1'
#     """
#
#     result = cursor.execute(query)
#     # print(result.fetchmany(size=3))
#     print(result.fetchall())
#
#     UPDATE ADSAJKDASJKLDHALDHASKJDHAKJHDSKLAJLHDKLASJHHKLSAJHLKSAJHD
#     query = """
#         UPDATE user
#         SET
#             address = 'Odessa'
#         WHERE
#             id > 2
#     """
#
#     query = """
#         UPDATE user
#         SET
#             address = LOWER ('mr_' || name || '@gmail.com'
#         WHERE
#             name LIKE '111%'
#     """
#
#
#     query = """
#         UPDATE user
#         SET
#             address = :Pass
#         WHERE
#             ib > 2
#     """
#     'eccbc87e4b5ce2fe28308fd9f2a7baf3'
#     cursor.execute(query, {'Pass': 'eccbc87e4b5ce2fe28308fd9f2a7baf3'})
#
#
# # RENAME TABLE
#     query = """
#         ALTER TABLE user
#         RENAME TO customers
#     """
#     cursor.execute(query)
# RENAME DISA:LKDJSALKJDSALKJDLKSAJDLKJSAKDSAJLKDJSLKAJDLSKJALKDJSALKJLKJL
# query = """
#     ALTER TABLE customers
#     RENAME COLUMN address TO email
# """
# cursor.execute(query)
#
# ADD COLUMN DKSLADSALKJDSLKJDLKSALJKDKSJALKJDLSKJALKJDLKJADSLKJALKJDSLAKJDLKJ
#
# query = """
#     ALTER TABLE customers
#     ADD COLUMN customers REAL
# """
# cursor.execute(query)
#
# query = """
#     UPDATE user
#     SET
#         balance = 0
#     WHERE
#         balance IS NULL
# """
#
# DELETE
# query = """
#     DELETE FROM customers
#     WHERE
#         name LIKE '1%'
# """
#
# cursor.execute(query)
#
#     sqlite_data = 'SELECT sqlite_version()'
#     cursor.execute(sqlite_data)
#     record = cursor.fetchall()
#     print(record)
#     print(connection.total_changes)

# login = input('Enter login')
# # fake_login', 'fake_pass'); INSERT INTO customers(name, login, password) VALUES ('M', 'DDDD', '2344');--
#
# query = f"""
#     INSERT INTO customer (name, login, password)
#     VALUES ('Axe', '{login}', 'kjsdkjlsdakjl')
# """
# cursor.execute(query)
