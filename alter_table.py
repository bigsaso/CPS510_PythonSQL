import connect
import cx_Oracle

cursor = connect.connection.cursor()
sql_alter = """
INSERT INTO try VALUES ('name')
"""

cursor.execute(sql_alter)
print('Table Altered.')