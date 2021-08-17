from tkinter import *

window = Tk()

def km_to_miles():
    print(e1_var.get())
    miles = float(e1_var.get())*1.606
    t1.insert(END,miles)

b1 = Button(window, text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1_var = StringVar()
e1 = Entry(window, textvariable=e1_var)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()