import connect
import cx_Oracle

cursor = connect.connection.cursor()
query = """
SELECT ROLE, COUNT(USER_ID) AS COUNT
    FROM usertb
    GROUP BY ROLE
"""

cursor.execute(query)
row = cursor.fetchall()
print(row)
print('Query Executed.')

#Closing cursor and connection
cursor.close()
connect.connection.close()