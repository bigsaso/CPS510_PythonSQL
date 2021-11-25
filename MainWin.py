from tkinter import *
#import connect
import cx_Oracle
import MainWin

root = Tk()
root.geometry("500x500")

#Creating window frames
login = Frame(root)
mainwindow = Frame(root)

#Creating function to switch window
def frameraise(frame):
    frame.tkraise()

#Creating function to manage frames
for frame in (login, mainwindow):
    frame.grid(row=0, column=0, sticky='news')

#Create function to manage login
def create_connection():
    #Creating global variables
    global username, password, cursor, connection
    username = user.get()
    password = pwd.get()
    #Creating connection with DBMS
    connection = cx_Oracle.connect(user=MainWin.username, password=MainWin.password, dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))")
    #Checking connection status
    if connection.version != 0:
        print(connection.version)
        cursor = connection.cursor()
        frameraise(mainwindow)

#Creating the function for when query_button is clicked:
def query_click():
    #Execute query.py
    exec(open('query.py').read())

#Creating the function for when insert_button is clicked:
def insert_click():
    #Execute query.py
    exec(open('create_table.py').read())

#Creating the function for when drop_button is clicked:
def drop_click():
    #Execute query.py
    exec(open('drop_table.py').read())

#Creating the function for when alter_button is clicked:
def alter_click():
    #Execute query.py
    exec(open('alter_table.py').read())

#Creating the function for when exit_button is clicked:
def exit_click():
    #Close cursor and connection
    cursor.close()
    connection.close()
    #Closing the app
    mainwindow.quit()
    login.quit()
    exit(0)

#Creating the GUI items for login
welcome = Label(login, text='Welcome to DBMS Python App. Please enter your username and password below')
user = Entry(login, width=50)
pwd = Entry(login, show='*', width=50)
login_button = Button(login, text='Login', command=create_connection)

#Creating the GUI items for main window
input = Entry(mainwindow, width=50)
query_button = Button(mainwindow, text='Query', command=query_click) #This button's function is defined by command query_click
insert_button = Button(mainwindow, text='Insert Table', command=insert_click) #This button's function is defined by command insert_click
drop_button = Button(mainwindow, text='Drop Table', command=drop_click) #This button's function is defined by command drop_click
alter_button = Button(mainwindow, text='Alter Table', command=alter_click) #This button's function is defined by command alter_click
exit_button = Button(mainwindow, text='Exit', command=exit_click) #This button's function is defined by command exit_click

#Creating the layout for login
welcome.grid(row=0, column=0)
user.grid(row=1, column=0)
pwd.grid(row=2, column=0)
login_button.grid(row=3, column=0)

#Creating the layout for main window
input.grid(row=0,column=0)
query_button.grid(row=1, column=0)
insert_button.grid(row=2, column=0)
drop_button.grid(row=3, column=0)
alter_button.grid(row=4, column=0)
exit_button.grid(row=5, column=0)

#Creating the window
frameraise(login)
root.mainloop()