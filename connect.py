import cx_Oracle
import db_config

#Creating connection with DBMS
connection = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
#Checking connection status
print(connection.version)