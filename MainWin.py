from tkinter import *
import connect, query

root = Tk()
root.geometry("500x200")
cursor = connect.connection.cursor()

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

#Creating the GUI items
welcome = Label(root, text='Welcome to DBMS Python App.')
input = Entry(root, width=50)
query_button = Button(root, text='Query', command=query_click) #This button's function is defined by command query_click
insert_button = Button(root, text='Insert Table', command=insert_click) #This button's function is defined by command insert_click
drop_button = Button(root, text='Drop Table', command=drop_click) #This button's function is defined by command drop_click
alter_button = Button(root, text='Alter Table', command=alter_click) #This button's function is defined by command alter_click

#Creating the layout
welcome.grid(row=0, column=0)
input.grid(row=1,column=0)
query_button.grid(row=2, column=0)
insert_button.grid(row=3, column=0)
drop_button.grid(row=4, column=0)
alter_button.grid(row=5, column=0)
#Creating the window
root.mainloop()