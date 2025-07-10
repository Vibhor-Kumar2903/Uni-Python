from SQL.database_connector import mysql_cursor

# creating table
mysql_cursor.execute("CREATE TABLE product (cid INTEGER(10), name VARCHAR(250), category VARCHAR(250), "
                     "price INTEGER(10), brand VARCHAR(100), rating FLOAT)")

mysql_cursor.close()
