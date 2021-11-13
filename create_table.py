import connect
import cx_Oracle

cursor = connect.connection.cursor()
sql_create = """
CREATE TABLE try(
    name varchar2(50)
)
"""

cursor.execute(sql_create)
print('Table Created.')

#Closing cursor and connection
cursor.close()
connect.connection.close()