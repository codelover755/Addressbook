from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

window = Tk()
window.title("Address book")

def clear_all():
    n_entry.delete(0,END)
    a_entry.delete(0,END)
    m_entry.delete(0,END)
    e_entry.delete(0,END)
    b_entry.delete(0,END)

myAddressBook = {}
def update():
    key = n_entry.get()
    if key not in myAddressBook.keys():
        book_list.insert(END,key)
    myAddressBook[key]=(n_entry.get(),a_entry.get(),m_entry.get(),e_entry.get(),b_entry.get())
    clear_all()

def display(event):
    new_w = Tk()
    index = book_list.curselection()
    display_content = Label(new_w)
    key = book_list.get(index)
    details = myAddressBook[key]
    contact = "Name: " + key + "\n" + "Address: " + details[0] + "\n" + "Mobile: " + details[1] + "\n" + "Email: " + details[2] + "\n" + "Email: " + details[3] + "\n" + "birthday: " + details[4]
    display_content.config(text=contact)
    display_content.grid(row=0,column=0)
    new_w.mainloop()

def save():
    s = asksaveasfile(defaultextension=".txt")
    print(myAddressBook,file=s)
    

address_title = Label(window,text="My Address Book")
n_label = Label(window,text="Name:")
a_label = Label(window,text="Address:")
m_label = Label(window,text="Mobile:")
e_label = Label(window,text="Email:")
b_label = Label(window,text="Birthday:")
book_list = Listbox(window,height=15,width=30)
book_list.bind('<<ListboxSelect>>',display)

n_entry = Entry(window, width=35)
a_entry = Entry(window, width=35)
m_entry = Entry(window, width=35)
e_entry = Entry(window, width=35)
b_entry = Entry(window, width=35)

o_button = Button(window,text="Open")
e_button = Button(window,text="Edit")
d_button = Button(window,text="Delete")
u_button = Button(window,text="Update/Add",command=update)
s_button = Button(window,text="Save",width=20, command=save)

address_title.grid(row=0,column=0,padx=20)
o_button.grid(row=0,column=1)
n_label.grid(row=1,column=1)
n_entry.grid(row=1,column=2)
a_label.grid(row=2,column=1)
a_entry.grid(row=2,column=2)
m_label.grid(row=3,column=1)
m_entry.grid(row=3,column=2)
b_label.grid(row=4,column=1)
b_entry.grid(row=4,column=2)
e_label.grid(row=5,column=1)
e_entry.grid(row=5,column=2)
e_button.grid(row=1,column=0)
d_button.grid(row=2,column=0)
u_button.grid(row=3,column=0)
s_button.grid(row=4,column=0)
book_list.grid(row=6,column=0)

window.mainloop()