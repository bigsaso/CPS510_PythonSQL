import connect
import MainWin
#import cx_Oracle

#cursor = connect.connection.cursor()
sql_alter = MainWin.input.get()
#sql_alter = """
#INSERT INTO try VALUES ('name')
#"""

MainWin.cursor.execute(sql_alter)
connect.connection.commit()
print('Table Altered.')

#Closing cursor and connection
#cursor.close()
#connect.connection.close()