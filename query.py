import connect
import cx_Oracle

cursor = connect.connection.cursor()
sql_drop = """
SELECT ROLE, COUNT(USER_ID) AS COUNT
    FROM usertb
    GROUP BY ROLE
"""

cursor.execute(sql_drop)
print('Query Executed.')