import tkinter as tk
from tkinter import *
import cx_Oracle
import app_v2

root = Tk()
root.title('Fantasy Soccer DBMS GUI')
root.geometry("570x310")

OPTIONS = [""]
# #[
# "Usertb","Usercred", "Team", "League", "Match", "Standings",
# "Goalkeeper", "Defender", "Midfielder", "Striker", "Lineup"
#]

#Creating window frames
login = Frame(root)
mainwindow = Frame(root)
query_page = Frame(root)
create_page = Frame(root)
alter_page = Frame(root)
drop_page = Frame(root)

#Creating function to switch window
def frameraise(frame):
    frame.tkraise()

#Creating function to manage frames
for frame in (login, mainwindow, query_page, alter_page, drop_page):
    frame.grid(row=0, column=0, sticky='news')

#Create function to manage login
def create_connection():
    #Creating global variables
    global username, password, cursor, connection
    username = user.get()
    password = pwd.get()
    #Creating connection with DBMS
    try:    
        #Tries to login using the information provided
        connection = cx_Oracle.connect(user=app_v2.username, password=app_v2.password, dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))")
    
        #Checking connection status
        if connection.version != 0:
            print(connection.version)
            cursor = connection.cursor()
            frameraise(mainwindow)
            result.config(width = 60, height = 5)
            cursor.execute("select table_name from user_tables order by table_name")
            optionList = cursor.fetchall()        
            for string in optionList:
                OPTIONS.append(string)
            OPTIONS.remove("")
            updateMenu()
    except:
        #Login information was incorrect, exception was thrown, prompt user again
        ins["text"] = "Invalid username/password. Please Try Again"   

        #Clears input fields 
        user.delete(0, END)
        pwd.delete(0, END)
    
#Creating the function for when query_button is clicked:
def query_click():
    query = 'select * from ' + table.get()
    result.config(state = NORMAL)
    if result.get('1.0',END) != '':
        result.delete('1.0', END)
    try: 
        cursor.execute(query)
        row = cursor.fetchall()
        result.insert(END, row)
    except:
        result.insert(END, "Query Command is incorrect or table does not exist")
    result.config(state = DISABLED)

#Creating the function for when insert_button is clicked:
def insert_click():
    sql_create = 'CREATE TABLE TRY (Name VARCHAR2(50), Age INT)'

    #Clears result Text if it isn't empty
    if result.get('1.0',END) != '':
            result.delete('1.0', END)

    try: 
        #Attempts to carry out input command, otherwise throw exception
        cursor.execute(sql_create)

        #Inform user Table was successfully created
        updateLabel['text'] = "Table Created"
        OPTIONS.append("TRY")
        updateMenu()
    except:
        updateLabel['text'] = "Table already exists"

#Creating the function for when drop_button is clicked:
def drop_click():
    sql_drop = "DROP TABLE TRY"

    try: 
        #Attempts to carry out input command, otherwise throw exception
        cursor.execute(sql_drop)
        updateLabel['text'] ='Table Dropped'
        OPTIONS.remove("TRY")
        updateMenu()
    except:
        updateLabel['text'] = "Table does not exist"

#Creating the function for when alter_button is clicked:
def alter_click():
    sql_alter = app_v2.input.get()
    #Enables result Text to be editted
    result.config(state = NORMAL)

    #Clears result Text if it isn't empty
    if result.get('1.0',END) != '':
            result.delete('1.0', END)

    try: 
        #Checks if entry is a alter/insert command, else throws exception
        if input.get().lower().find('alter') == -1 and input.get().lower().find('insert'):
            raise ValueError

        #Attempts to carry out input command, otherwise throw exception
        cursor.execute(sql_alter)
        connection.commit()
        result.insert(END, 'Table Altered')
    except ValueError:
        result.insert(END, "Please enter an alter/insert command")
    except:
        result.insert(END, "Alter command is incorrect or this table does not exist")
    result.config(state = DISABLED)

#Creating the function for when exit_button is clicked:
def exit_click():
    #Close cursor and connection
    cursor.close()
    connection.close()
    #Closing the app
    close_window()

#Creating a function to close the window 
def close_window():
    query_page.quit()
    mainwindow.quit()
    login.quit()
    exit(0)

#Creating the function to prompt user in input field
def on_entry_click(event):
    if input.get() == "Enter your command...":
        input.delete(0 , 'end')

def updateMenu ():
    tables_ddown["menu"].delete(0, "end")
    for string in OPTIONS:
        tables_ddown["menu"].add_command(label = string, command = tk._setit(table,string))
    
    table.set(OPTIONS[0]) # default value
        

#Changes the behaviour of the [x] button to run close_window when clicked (previously, clicking [x] button made another instance open)
root.protocol("WM_DELETE_WINDOW", close_window)

#Creating the GUI items for login
welcome = Label(login, text='Welcome to DBMS Python App.')
ins = Label (login, text = "Please enter your username and password below")

#Created a frame to hold label and entry widgets together for user field
user_frame = tk.Frame(login)
user_text = Label(user_frame, text='Username')
user = Entry(user_frame, width=20)
user_text.pack(side = LEFT, padx = 5)
user.pack(side = RIGHT, padx = 5)

#Created a frame to hold label and entry widgets together for password field
pass_frame = tk.Frame (login)
pass_text = Label(pass_frame, text='Password')
pwd = Entry(pass_frame, show='*', width=20)
pass_text.pack(side = LEFT, padx = 5)
pwd.pack(side = RIGHT, padx = 5)

login_button = Button(login, text='Login', command=create_connection)

#Creating the GUI items for main window
#input = Entry(mainwindow, width=50)
#input.insert(0, "Enter your command...")
#input.bind('<FocusIn>', on_entry_click)
to_query = Button(mainwindow, text='Go to Query page', width=30, command=lambda : frameraise(query_page))
to_create = Button(mainwindow, text='Go to Create Table page', width=30, command=insert_click)
to_alter = Button(mainwindow, text='Go to Alter Table page', width=30, command=lambda : frameraise(alter_page))
to_drop = Button(mainwindow, text='Go to Drop Table page', width=30, command=drop_click)
introLabel = Label (mainwindow, text ="Welcome to the Fantasy Soccer DBMS")
updateLabel = Label (mainwindow, text = "Please select an option")
#query_button1 = Button(mainwindow, text='Query', width = 30, command=query_click2) #This button's function is defined by command query_click
#insert_button = Button(mainwindow, text='Create Table',width = 30, command=insert_click) #This button's function is defined by command insert_click
#drop_button = Button(mainwindow, text='Drop Table',width = 30, command=drop_click) #This button's function is defined by command drop_click
#alter_button = Button(mainwindow, text='Alter Table/Insert',width = 30, command=alter_click) #This button's function is defined by command alter_click
exit_button = Button(mainwindow, text='Exit',width = 30, command=exit_click) #This button's function is defined by command exit_click
#result1 = Text(mainwindow, wrap= WORD, height =0, width = 0, state = DISABLED)

#Creating the GUI for query page
back_button = Button(query_page, text='Back', width=30, command=lambda : frameraise(mainwindow))
query_button = Button(query_page, text='Query', width = 30, command=query_click) #This button's function is defined by command query_click
result = Text(query_page, wrap= WORD, height =0, width = 0, state = DISABLED)
table = StringVar(query_page)
tables_ddown = OptionMenu(query_page, table, *OPTIONS)


#Creating the GUI for create table page
back_button1 = Button(create_page, text='Back', width=30, command=lambda : frameraise(mainwindow))
insert_button = Button(create_page, text='Create Table',width = 30, command=insert_click) #This button's function is defined by command insert_click
result1 = Text(create_page, wrap= WORD, height =0, width = 0, state = DISABLED)
#table = StringVar(query_page)
#table.set(OPTIONS[0]) # default value
#tables_ddown = OptionMenu(query_page, table, *OPTIONS)

#Creating the GUI for alter table page
back_button2 = Button(alter_page, text='Back', width=30, command=lambda : frameraise(mainwindow))
alter_button = Button(alter_page, text='Alter Table/Insert',width = 30, command=alter_click) #This button's function is defined by command alter_click
result2 = Text(alter_page, wrap= WORD, height =0, width = 0, state = DISABLED)
#table = StringVar(query_page)
#table.set(OPTIONS[0]) # default value
#tables_ddown = OptionMenu(query_page, table, *OPTIONS)

#Creating the GUI for drop table page
back_button3 = Button(drop_page, text='Back', width=30, command=lambda : frameraise(mainwindow))
drop_button = Button(drop_page, text='Drop Table',width = 30, command=drop_click) #This button's function is defined by command drop_click
result3 = Text(drop_page, wrap= WORD, height =0, width = 0, state = DISABLED)
#table = StringVar(query_page)
#table.set(OPTIONS[0]) # default value
#tables_ddown = OptionMenu(query_page, table, *OPTIONS)

#Creating the layout for login
login.columnconfigure(0, weight = 1, minsize= 570)
for i in range (0,5):
    login.rowconfigure(i, weight = 1, minsize=10)
welcome.grid(row = 0, column = 0, padx = 0, pady = 20, sticky="n")
ins.grid (row = 1, column = 0, padx = 0, pady = 5, sticky = "n")
user_frame.grid(row =2, column = 0, padx = 0, pady = 5, sticky = "n")
pass_frame.grid(row = 3, column = 0, padx= 0, pady = 5, sticky = "n")
login_button.grid(row = 4, column = 0, padx = 0, pady = 5, sticky="n")

#Creating the layout for main window
mainwindow.columnconfigure(0, weight = 1, minsize= 570)
#result1.grid(row =0, column = 0, padx = 5, pady = 5, sticky = "n")
#input.grid(row=1,column=0, padx=5, pady=5, sticky="ns")
#query_button1.grid(row=7, column=0, padx=5, pady=5, sticky="ns")
introLabel.grid(row = 0, column = 0, pady=5, padx=5, sticky="ns")
updateLabel.grid(row = 1, column = 0, pady=5, padx=5, sticky="ns")
to_query.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
to_create.grid(row=3, column=0, padx=5, pady=5, sticky="ns")
to_alter.grid(row=4, column=0, padx=5, pady=5, sticky="ns")
to_drop.grid(row=5, column=0, padx=5, pady=5, sticky="ns")
#insert_button.grid(row=3, column=0, padx=5, pady=5, sticky="ns")
#drop_button.grid(row=4, column=0, padx=5, pady=5, sticky="ns")
#alter_button.grid(row=5, column=0, padx=5, pady=5, sticky="ns")
exit_button.grid(row=6, column=0, padx=5, pady=5, sticky="ns")

#Creating the layout for query page
query_page.columnconfigure(0, weight = 1, minsize= 570)
result.grid(row =0, column = 0, padx = 5, pady = 5, sticky = "n")
tables_ddown.grid(row=1, column=0, padx=5, pady=5, sticky="n")
query_button.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
back_button.grid(row=3, column=0, padx=5, pady=5, sticky="ns")

#Creating the layout for create table page
create_page.columnconfigure(0, weight = 1, minsize= 570)
result1.grid(row =0, column = 0, padx = 5, pady = 5, sticky = "n")
#tables_ddown.grid(row=1, column=0, padx=5, pady=5, sticky="n")
insert_button.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
back_button1.grid(row=3, column=0, padx=5, pady=5, sticky="ns")

#Creating the layout for alter table page
alter_page.columnconfigure(0, weight = 1, minsize= 570)
result2.grid(row =0, column = 0, padx = 5, pady = 5, sticky = "n")
#tables_ddown.grid(row=1, column=0, padx=5, pady=5, sticky="n")
alter_button.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
back_button2.grid(row=3, column=0, padx=5, pady=5, sticky="ns")

#Creating the layout for drop table page
drop_page.columnconfigure(0, weight = 1, minsize= 570)
result3.grid(row =0, column = 0, padx = 5, pady = 5, sticky = "n")
#tables_ddown.grid(row=1, column=0, padx=5, pady=5, sticky="n")
drop_button.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
back_button3.grid(row=3, column=0, padx=5, pady=5, sticky="ns")

#Creating the window
frameraise(login)
root.mainloop()