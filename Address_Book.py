from tkinter import *
import tkinter.messagebox as mb


root = Tk()
root.title("Address Book")
root.geometry('700x550')

# Creating the color and font variables
lf_bg = 'cadet blue'
rf_bg = 'cadet blue3'
nf_bg = 'cyan3'
frame_font = ("Verdana", 14)

# Creating the variables
addressbook = []
LastName = StringVar()
FirstName = StringVar()
Address = StringVar()
Number = StringVar()
Search = StringVar()

# Creating and placing the components in the main window
Label(root, text='Address Book', font=("Verdana", 15, "bold"), bg='cadet blue4', fg='black').pack(side=TOP, fill=X)

# Setting up the frame of the main window
left_frame = Frame(root, bg=lf_bg)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)

right_frame = Frame(root, bg=rf_bg)
right_frame.place(relx=0.3, relwidth=0.8, relheight=1, y=30)

# Function for getting a selected value
def click():
    return int(select.curselection()[0])

# Function for getting the entry number
def entry_num():
    return delete_entry.get()

# Function for opening a window to add a contact
def Open_Add():
    select.delete(0, END)
    global add
    add = Toplevel()
    add.title("Adding Contact")
    add.geometry('400x550')

    add_frame = Frame(add, bg=nf_bg)
    add_frame.place(relx=0, relheight=1, y=30, relwidth=1)

    global LastName, FirstName, Address, Number

    Button(add_frame, text='Save Contact', font='Verdana 10', width=15, command=Add_Contact).place(relx=0.07, rely=0.7)
    Button(add_frame, text='Exit', font='Verdana 10', width=15, command=add.destroy).place(relx=0.07, rely=0.8)

    Label(add_frame, text='Last Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.05)
    lastname_entry = Entry(add_frame, width=35, font=("Verdana", 12), textvariable=LastName)
    lastname_entry.place(relx=0.05, rely=0.1)

    Label(add_frame, text='First Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.2)
    firstname_entry = Entry(add_frame, width=35, font=("Verdana", 12), textvariable=FirstName)
    firstname_entry.place(relx=0.05, rely=0.25)

    Label(add_frame, text='Address', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.35)
    address_entry = Entry(add_frame, width=35, font=("Verdana", 12), textvariable=Address)
    address_entry.place(relx=0.05, rely=0.4)

    Label(add_frame, text='Contact Number', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.5)
    number_entry = Entry(add_frame, width=35, font=("Verdana", 12), textvariable=Number)
    number_entry.place(relx=0.05, rely=0.55)


# Function for adding a contact
def Add_Contact():
    global addressbook, add
    addressbook.append([LastName.get(), FirstName.get(), Address.get(), Number.get()])
    mb.showinfo('Contact added', 'We have stored the contact successfully!')
    Reset()
    add.destroy()

# Function for showing a contact's details
def Show_Details():
    view = Toplevel()
    view.title("Viewing a Contact")
    view.geometry('400x550')

    view_frame = Frame(view, bg=nf_bg)
    view_frame.place(relx=0, relheight=1, y=30, relwidth=1)

    LNAME, FNAME, ADD, NUMB = addressbook[click()]
    LastName.set(LNAME)
    FirstName.set(FNAME)
    Address.set(ADD)
    Number.set(NUMB)

    Label(view_frame, text='Last Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.05)
    lastname_entry = Entry(view_frame, width=35, font=("Verdana", 12), textvariable=LastName)
    lastname_entry.place(relx=0.05, rely=0.1)

    Label(view_frame, text='First Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.2)
    firstname_entry = Entry(view_frame, width=35, font=("Verdana", 12), textvariable=FirstName)
    firstname_entry.place(relx=0.05, rely=0.25)

    Label(view_frame, text='Address', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.35)
    address_entry = Entry(view_frame, width=35, font=("Verdana", 12), textvariable=Address)
    address_entry.place(relx=0.05, rely=0.4)

    Label(view_frame, text='Contact Number', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.5)
    number_entry = Entry(view_frame, width=35, font=("Verdana", 12), textvariable=Number)
    number_entry.place(relx=0.05, rely=0.55)

    Button(view_frame, text='Exit', font='Verdana 10', width=15, command=view.destroy).place(relx=0.07, rely=0.8)

# Function for saving changes in editing a contact
def Update_Contact():
    global lastname_edit, firstname_edit, number_edit, address_edit, edit_entry
    addressbook[int(edit_entry)] = [lastname_edit.get(), firstname_edit.get(), number_edit.get(), address_edit.get()]
    mb.showinfo('Contact Updated', 'The contact has been edited')

    View_Contacts()

# Function for editing a contact
def Edit_Contact():
    select.delete(0, END)

    edit = Toplevel()
    edit.title("Editing a Contact")
    edit.geometry('400x550')

    edit_frame = Frame(edit, bg=nf_bg)
    edit_frame.place(relx=0, relheight=1, y=30, relwidth=1)


    global lastname_edit, firstname_edit, number_edit, address_edit, edit_entry

    edit_entry = entry_num()
    LNAME, FNAME, ADD, NUMB = addressbook[int(edit_entry)]
    LastName.set(LNAME)
    FirstName.set(FNAME)
    Address.set(ADD)
    Number.set(NUMB)

    Label(edit_frame, text='Last Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.05)
    lastname_edit = Entry(edit_frame, width=35, font=("Verdana", 12), textvariable=LastName)
    lastname_edit.place(relx=0.05, rely=0.1)

    Label(edit_frame, text='First Name', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.2)
    firstname_edit = Entry(edit_frame, width=35, font=("Verdana", 12), textvariable=FirstName)
    firstname_edit.place(relx=0.05, rely=0.25)

    Label(edit_frame, text='Address', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.35)
    address_edit = Entry(edit_frame, width=35, font=("Verdana", 12), textvariable=Address)
    address_edit.place(relx=0.05, rely=0.4)

    Label(edit_frame, text='Contact Number', bg='cyan3', font=frame_font).place(relx=0.1, rely=0.5)
    number_edit = Entry(edit_frame, width=35, font=("Verdana", 12), textvariable=Number)
    number_edit.place(relx=0.05, rely=0.55)

    Button(edit_frame, text='Save Changes', font='Verdana 10', width=15, command=Update_Contact).place(relx=0.07, rely=0.7)
    Button(edit_frame, text='Exit', font='Verdana 10', width=15, command=edit.destroy).place(relx=0.07, rely=0.8)

    delete_entry.delete(0, END)

# Function for deleting a contact
def Delete_Contact():
    
    edit_entry = entry_num()
    addressbook.pop(int(edit_entry))
    mb.showinfo('Contact deleted', 'The contact has been deleted')
    
    View_Contacts()
    delete_entry.delete(0, END)

# Function for opening a window to search a contact
def Open_Search():
    select.delete(0, END)
    global sear

    sear = Toplevel()
    sear.title("Search a Contact")
    sear.geometry('300x300')


    sear_frame = Frame(sear, bg=nf_bg)
    sear_frame.place(relx=0, relheight=1, y=30, relwidth=1)

    global Search, user_option

    search_option = ["Last Name", "First Name", "Address", "Contact Number"]
    user_option = StringVar()
    OptionMenu(sear, user_option, * search_option).place(relx=0.4, rely=0.15)

    Label(sear, text='Search by:', font=("Verdana", 10), bg=nf_bg).place(relx=0.1, rely=0.15)

    search_entry = Entry(sear_frame, width=25, font=("Verdana", 12), textvariable=Search)
    search_entry.place(relx=0.1, rely=0.3)

    Button(sear_frame, text='Search', font='Verdana 10', width=15, command=Search_Contact).place(relx=0.07, rely=0.4)
    Button(sear_frame, text='Exit', font='Verdana 10', width=15, command=sear.destroy).place(relx=0.07, rely=0.5)

    search_entry.delete(0, END)

# Function for searching a contact
def Search_Contact():
    global user_option, sear
    search_choices = user_option.get()
    user_search = str(Search.get())

    
    if search_choices == "Last Name":
        for l, f, a, n in addressbook:
            if user_search == l:
                mb.showinfo('Contact Exist', 'Press OK to view result')
                select.insert(END, [l, f])  
            else:
                mb.showinfo('Error', 'The contact does not exist')           
    elif search_choices == "First Name":
        for l, f, a, n in addressbook:
            if user_search == f:
                mb.showinfo('Contact Exist', 'Press OK to view result')
                select.insert(END, [l, f])
            else:
                mb.showinfo('Error', 'The contact does not exist')
    elif search_choices == "Address":
        for l, f, a, n in addressbook:
            if user_search == a:
                mb.showinfo('Contact Exist', 'Press OK to view result')
                select.insert(END, [l, f])
            else:
                mb.showinfo('Error', 'The contact does not exist')
    elif search_choices == "Contact Number":
        for l, f, a, n in addressbook:
            if user_search == n:
                mb.showinfo('Contact Exist', 'Press OK to view result')
                select.insert(END, [l, f])
            else:
                mb.showinfo('Error', 'The contact does not exist')

    sear.destroy()

# Function for showing the entire contact list
def View_Contacts():
    select.delete(0, END)
    for l, f, a, n in addressbook:
        select.insert(END, [l, f])

# Function for clearing an entry box
def Reset():
    LastName.set('')
    FirstName.set('')
    Address.set('')
    Number.set('')

# Function for closing window
def Exit():
    root.destroy()

# Setting up the listbox
scrollbar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scrollbar.set, height=14)
scrollbar.config (command=select.yview)
scrollbar.pack(side=RIGHT, fill=Y)
select.place(relx=0.4, rely=0.25, width=350)

# Setting up the left frame
Label(root, text='What would you\nlike to do?', font=("Verdana", 12), bg=lf_bg, fg='black').place(relx=0.07, rely=0.1)
Button(left_frame, text='Add Contact', font=frame_font, width=15, command=Open_Add).place(relx=0.07, rely=0.15)
Button(left_frame, text='Edit Contact', font=frame_font, width=15, command=Edit_Contact).place(relx=0.07, rely=0.25)
Button(left_frame, text='Delete Contact', font=frame_font, width=15, command=Delete_Contact).place(relx=0.07, rely=0.35)
Button(left_frame, text='View Contacts', font=frame_font, width=15, command=View_Contacts).place(relx=0.07, rely=0.45)
Button(left_frame, text='Search', font=frame_font, width=15, command=Open_Search).place(relx=0.07, rely=0.55)
Button(left_frame, text='Exit', font=frame_font, width=15, command=exit).place(relx=0.07, rely=0.65)

# Setting up the right frame
Label(right_frame, text='List of Contacts', font=("Verdana", 12, "bold"), bg=rf_bg).place(relx=0.32, rely=0.03)
Label(right_frame, text='Entry Number:\n(Starting number is 0)', font=("Verdana", 10), bg=rf_bg).place(relx=0.03, rely=0.08)
delete_entry = Entry(right_frame, width=20, font=("Verdana", 12))
delete_entry.place(relx=0.35, rely=0.1)
Button(right_frame, text='View Contact Details', font='Verdana 10', width=19, command=Show_Details).place(relx=0.10, rely=0.85)

root.update()

root.mainloop()