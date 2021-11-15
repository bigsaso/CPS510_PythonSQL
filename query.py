#import connect
import MainWin
#import cx_Oracle

#cursor = connect.connection.cursor()
query = MainWin.input.get()

MainWin.cursor.execute(query)
row = MainWin.cursor.fetchall()
print(row)
print('Query Executed.')

#Closing cursor and connection
#cursor.close()
#connect.connection.close()