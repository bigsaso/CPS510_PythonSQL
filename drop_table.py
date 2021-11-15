#import connect
import MainWin
#import cx_Oracle

#cursor = connect.connection.cursor()
sql_drop = MainWin.input.get()
#sql_drop = """
#DROP TABLE try
#"""

MainWin.cursor.execute(sql_drop)
print('Table Dropped.')

#Closing cursor and connection
#cursor.close()
#connect.connection.close()