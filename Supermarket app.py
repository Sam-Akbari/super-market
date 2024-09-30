#برنامه سوپر مارکتی

from tkinter import *
from tkinter import messagebox

def add_item():
    item_name = name.get()
    item_mogodi = mogodi.get()
    if item_name and item_mogodi:
        lists.insert(END, f"{item_name} - {item_mogodi}")
        name.delete(0, END)
        mogodi.delete(0, END)
    else:
        messagebox.showwarning("SuperMarket App!", "Enter (name) and (mogodi) please!")

def delete_item():
    selected_item = lists.curselection()
    if selected_item:
        lists.delete(selected_item)
    else:
        messagebox.showwarning("SuperMarket App!", "Select an item to delete please!")

def edit_item():
    selected_item = lists.curselection()
    if selected_item:
        item_name = name.get()
        item_mogodi = mogodi.get()
        if item_name and item_mogodi:
            lists.delete(selected_item)
            lists.insert(selected_item, f"{item_name} - {item_mogodi}")
            name.delete(0, END)
            mogodi.delete(0, END)
        else:
            messagebox.showwarning("SuperMarket App!", "Enter (name) and (mogodi) please!")
    else:
        messagebox.showwarning("SuperMarket App!", "Select an item to edit please!")

def close_app():
    shop.destroy()

def search_item():
    search = Tk()
    search.title("Search bar")
    search.geometry("400x150")
    search.resizable(0,0)
    search.config(bg="light green")
    search_entry = Entry(search, width=50)
    search_entry.place(x=10, y=50)

    def perform_search():
        search_term = search_entry.get()
        search_results.delete(0, END)
        for item in lists.get(0, END):
            if search_term.lower() in item.lower():
                search_results.insert(END, item)

    search_label1 = Label(search, text="Search bar", bg="light green",fg="blue",font=(20)).place(x=150, y=15)
    search_button = Button(search, text="Search", command=perform_search,width=8,height=1,fg="blue").place(x=320, y=50)
    search_label2 =  Label(search, text="Your search:", bg="light green").place(x=9, y=75)
    search_results = Listbox(search, width=60, height=1)
    search_results.place(x=16, y=100)

shop = Tk()
shop.config(bg="light green")
shop.title("SuperMarket App")
shop.geometry("500x480")
shop.resizable(0, 0)

text = Label(shop, text="Welcome to Supermarket app!", font=(200), bg="light green", fg="red").place(x=100, y=20)

text_name = Label(shop, text="< Name", bg="light green").place(x=268, y=70)
text_mogodi = Label(shop, text="< mogodi", bg="light green").place(x=260, y=100)

name = Entry(shop, width=40)
name.place(x=10, y=70)
mogodi = Entry(shop, width=40)
mogodi.place(x=10, y=100)

lists = Listbox(shop, width=50, height=20)
lists.place(x=10, y=130)

add = Button(shop, text="Add", fg="green", width=23, height=4, command=add_item).place(x=320, y=70)
search = Button(shop, text="Search", fg="blue", width=23, height=4, command=search_item).place(x=320, y=150)
delet = Button(shop, text="Delet", fg="red", width=23, height=4, command=delete_item).place(x=320, y=230)
edit = Button(shop, text="Edit", fg="purple", width=23, height=4, command=edit_item).place(x=320, y=310)
close = Button(shop, text="Close App", fg="orange", width=23, height=4, command=close_app).place(x=320, y=390)

shop.mainloop()

#این برنامه در گیت هاب و کوئرا اپلود شده