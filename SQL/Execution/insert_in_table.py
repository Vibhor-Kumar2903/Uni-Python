from SQL.database_connector import *

# insert values in table
table = ("INSERT INTO product (cid, name, category, price, brand, rating)"
         "VALUES (%s, %s, %s, %s, %s, %s)")

# values = (1, 'Blue Shirt', 'clothing', 750, 'Denim', 3.8)


values = (1, 'Blue Shirt', 'clothing', 750, 'Denim', 3.8)


executed = mysql_cursor.execute(table, values)
connect_db.commit()
connect_db.close()
