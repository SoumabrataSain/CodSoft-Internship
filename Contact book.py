from tkinter import *
root = Tk()
root.geometry('550x350')
Name = StringVar()
Number = StringVar()
contacts = []

def search_contact():
    search_term = Name.get() or Number.get()
    results = [contact for contact in contacts if search_term in contact.values()]
    select.delete(0, END)
    for result in results:
        select.insert(END, f"{result['name']} - {result['number']}")

def add_contact():
    name = Name.get()
    number = Number.get()
    contacts.append({'name': name, 'number': number})
    Name.set("")
    Number.set("")
    update_contact_list()

def view_contact():
    update_contact_list()

def delete_contact():
    selected_index = select.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        update_contact_list()

def update_contact():
    selected_index = select.curselection()
    if selected_index:
        index = selected_index[0]
        new_name = Name.get()
        new_number = Number.get()
        contacts[index] = {'name': new_name, 'number': new_number}
        Name.set("")
        Number.set("")
        update_contact_list()

def update_contact_list():
    select.delete(0, END)
    for contact in contacts:
        select.insert(END, f"{contact['name']} - {contact['number']}")

main_frame = Frame(root)
main_frame.pack()

entry_frame = Frame(main_frame)
entry_frame.pack()

name_label = Label(entry_frame, text = 'Name', font='arial 12 bold')
name_label.pack(side=LEFT)
name_entry = Entry(entry_frame, textvariable=Name, width=50)
name_entry.pack()

phone_label = Label(entry_frame, text = 'Phone No.', font='arial 12 bold')
phone_label.pack(side=LEFT)
phone_entry = Entry(entry_frame, textvariable=Number, width=50)
phone_entry.pack()

button_frame = Frame(main_frame)
button_frame.pack()

search_button = Button(button_frame, text="Search", font="arial 12 bold", command=search_contact)
search_button.pack(side=LEFT, padx=10)
add_button = Button(button_frame, text="Add", font="arial 12 bold", command=add_contact)
add_button.pack(side=LEFT, padx=10)
view_button = Button(button_frame, text="View", font="arial 12 bold", command=view_contact)
view_button.pack(side=LEFT, padx=10)
delete_button = Button(button_frame, text="Delete", font="arial 12 bold", command=delete_contact)
delete_button.pack(side=LEFT, padx=10)
update_button = Button(button_frame, text="Update", font="arial 12 bold", command=update_contact)
update_button.pack(side=LEFT, padx=10)

list_frame = Frame(root)
list_frame.pack()

scroll_bar = Scrollbar(list_frame, orient=VERTICAL)
select = Listbox(list_frame, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
select.pack(side=LEFT, fill=BOTH)
scroll_bar.pack(side=RIGHT, fill=Y)

root.mainloop()