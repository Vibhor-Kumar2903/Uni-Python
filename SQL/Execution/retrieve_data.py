from SQL.database_connector import *

# Retrieve data form table

retrieve_data = "select * from product;"

mysql_cursor.execute(retrieve_data)

rows = mysql_cursor.fetchall()

print(rows)

for row in rows:
    print(row)

connect_db.commit()
connect_db.close()
