#import connect
import MainWin
#import cx_Oracle

#cursor = connect.connection.cursor()
sql_create = MainWin.input.get()
#sql_create = """
#CREATE TABLE try(
#    name varchar2(50)
#)
#"""

MainWin.cursor.execute(sql_create)
print('Table Created.')

#Closing cursor and connection
#cursor.close()
#connect.connection.close()