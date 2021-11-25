from tkinter import *
import cx_Oracle
import MainWin

root = Tk()
root.title('SQL GUI')
root.geometry("570x310")

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
    query = input.get()
    cursor.execute(query)
    row = cursor.fetchall()
    result = Text(mainwindow, height=10)
    result.grid(row=6, column=0)
    result.insert(END, row)

#Creating the function for when insert_button is clicked:
def insert_click():
    sql_create = input.get()
    cursor.execute(sql_create)
    created = Label(mainwindow, text='Table Created')
    created.grid(row=6, column=0)

#Creating the function for when drop_button is clicked:
def drop_click():
    sql_drop = MainWin.input.get()
    cursor.execute(sql_drop)
    deleted = Label(mainwindow, text='Table Dropped')
    deleted.grid(row=6, column=0)

#Creating the function for when alter_button is clicked:
def alter_click():
    sql_alter = MainWin.input.get()
    cursor.execute(sql_alter)
    connection.commit()
    altered = Label(mainwindow, text='Table Altered')
    altered.grid(row=6, column=0)

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
user_text = Label(login, text='Username')
pass_text = Label(login, text='Password')
user = Entry(login, width=20)
pwd = Entry(login, show='*', width=20)
login_button = Button(login, text='Login', command=create_connection)

#Creating the GUI items for main window
input = Entry(mainwindow, width=50)
query_button = Button(mainwindow, text='Query', command=query_click) #This button's function is defined by command query_click
insert_button = Button(mainwindow, text='Create Table', command=insert_click) #This button's function is defined by command insert_click
drop_button = Button(mainwindow, text='Drop Table', command=drop_click) #This button's function is defined by command drop_click
alter_button = Button(mainwindow, text='Alter Table', command=alter_click) #This button's function is defined by command alter_click
exit_button = Button(mainwindow, text='Exit', command=exit_click) #This button's function is defined by command exit_click

#Creating the layout for login
welcome.pack()
user_text.pack(pady=5)
user.pack(padx=5)
pass_text.pack(pady=5)
pwd.pack(padx=5)
login_button.pack(pady=5)

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