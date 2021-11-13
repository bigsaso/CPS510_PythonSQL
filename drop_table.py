import connect
import cx_Oracle

cursor = connect.connection.cursor()
sql_drop = """
DROP TABLE try
"""

cursor.execute(sql_drop)
print('Table Dropped.')

#Closing cursor and connection
cursor.close()
connect.connection.close()