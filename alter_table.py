import connect
import cx_Oracle

cursor = connect.connection.cursor()
sql_alter = """
INSERT INTO try VALUES ('name')
"""

cursor.execute(sql_alter)
connect.connection.commit()
print('Table Altered.')

#Closing cursor and connection
cursor.close()
connect.connection.close()