import cx_Oracle

#Creating connection with DBMS
connection = cx_Oracle.connect('slogozzo/11236504@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca')
#Checking connection status
print(connection.version)