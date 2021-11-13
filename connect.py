import cx_Oracle

#Creating connection with DBMS
connection = cx_Oracle.connect('slogozzo/11236504@//oracle.scs.ryerson.ca:1521/orcl')
#Checking connection status
print(connection.version)