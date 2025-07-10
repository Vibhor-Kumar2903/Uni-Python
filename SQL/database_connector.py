from mysql.connector import connect

connect_db = connect(host="localhost",
                     user="root",
                     passwd="Vibh@29#03",
                     database="product")

mysql_cursor = connect_db.cursor()

if mysql_cursor:
    print(f"Connection Established....")
else:
    print(f"Unable to established connection...")

