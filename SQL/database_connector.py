from mysql.connector import connect

connect_db = connect(host="localhost",
                     user="root",
                     passwd="Vibh@29#03")

mysql_cursor = connect_db.cursor()

if mysql_cursor:
    print(f"mysql_cursor :: {mysql_cursor}")
    print(f"Connection Established....")

