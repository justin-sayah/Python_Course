"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search and entry
Add entry
Update entry
Delete
Close
"""

import sqlite3
from tkinter import *
import backend

#Open a Tkinter Window and title it bookstore
window = Tk()
window.wm_title("BookStore")

# The idea is to use a grid-like GUI to lay out labels and text entry windows
# for inputting book information
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

#ListBox where the database is actively displayed and can be interacted with
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#Scrollbar for controlling the ListBox
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list1.yview())

#Method that displays the information of a selected database 
# row in the entry windows above when selected with the mouse
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

list1.bind('<<ListboxSelect>>', get_selected_row)

#Displays all entries in the database in the ListBox object
def view_command():
    #Empties the ListBox
    list1.delete(0,END)
    for row in backend.view():
        #Displays each row returned from backend.view() within the ListBox
        list1.insert(END, row)

#Gets text inserted into the entry boxes and searches the database. displaying matching entries
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

#Gets text inserted into the entry boxes and inserts it into the database
#Displays new entry in the ListBox
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    view_command()

#Updates a selected row in the ListBox with updated text in the entry fields
def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

#Deletes a selected row from the ListBox
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

#These lines bind the commands above to the button elements that are created
#and displayed on the GUI
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()