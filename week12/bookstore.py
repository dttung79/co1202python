from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
books = {'Python Programming': ['John Smith', 205],
         'Software Engineering': ['Mary Jane', 150],
         'Harry Potter': ['J.K. Rowling', 300],
         'Homo Sapiens': ['Donald Trump', 180]}
### EVENT HANDLERS ###
def lst_books_selected(event):
    name = lst_books.get(lst_books.curselection())
    author = books[name][0]
    price = books[name][1]
    txt_name.delete(0, END)
    txt_name.insert(0, name)
    txt_author.delete(0, END)
    txt_author.insert(0, author)
    txt_price.delete(0, END)
    txt_price.insert(0, price)

def btn_ok_clicked():
    price = float(txt_price.get())
    quantity = int(txt_quantity.get())
    payment = price * quantity

    deliver_method = cbb_delivers.current()
    if deliver_method == 0: # standard
        payment += 1
    elif deliver_method == 1: # fast
        payment += 2
    else: # express
        payment += 5

    if cover_choice.get() == True:
        payment += 2
    
    messagebox.showinfo('Payment', f'Total payment: ${payment}')

def btn_cancel_clicked():
    txt_name.delete(0, END)
    txt_price.delete(0, END)
    txt_author.delete(0, END)
    txt_quantity.delete(0, END)
    
### CREATE WINDOW & WIDGETS ###
window = Tk()
window.title("Bookstore")
window.geometry("500x300")

lbl_books = Label(window, text="Books")
lbl_books.grid(row=0, column=0, sticky=W, padx=10)

lst_books = Listbox(window, width=20, height=5, selectmode=SINGLE)
lst_books.grid(row=1, column=0, sticky=W, columnspan=2, rowspan=3, padx=10)
for i, book in enumerate(books.keys()):
    lst_books.insert(i, book)
lst_books.bind("<<ListboxSelect>>", lst_books_selected)

lbl_name = Label(window, text="Name")
lbl_name.grid(row=1, column=2, sticky=W)
txt_name = Entry(window, width=20)
txt_name.grid(row=1, column=3, sticky=W, columnspan=2)

lbl_author = Label(window, text="Author")
lbl_author.grid(row=2, column=2, sticky=W)
txt_author = Entry(window, width=20)
txt_author.grid(row=2, column=3, sticky=W, columnspan=2)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=3, column=2, sticky=W)
txt_price = Entry(window, width=20)
txt_price.grid(row=3, column=3, columnspan=2)

lbl_quantity = Label(window, text='Quantity')
lbl_quantity.grid(row=4, column=0, sticky=W, padx=10)
txt_quantity = Entry(window, width=8)
txt_quantity.grid(row=4, column=1, sticky=W)

lbl_deliver = Label(window, text='Deliver')
lbl_deliver.grid(row=5, column=0, sticky=W, padx=10)

cbb_delivers = Combobox(window, width=8)
cbb_delivers['values'] = ['Standard ($1)', 'Fast ($2)', 'Express ($5)']
cbb_delivers.grid(row=5, column=1, sticky=W)
cbb_delivers.current(0)

lbl_cover = Label(window, text='Cover ($2)')
lbl_cover.grid(row=5, column=2, sticky=W)

cover_choice = IntVar()
cover_choice.set(0) # by default no cover
rd_cover_yes = Radiobutton(window, text='Yes', value=1, variable=cover_choice)
rd_cover_yes.grid(row=5, column=3, sticky=W)
rd_cover_no = Radiobutton(window, text='No', value=0, variable=cover_choice)
rd_cover_no.grid(row=5, column=4, sticky=W)

btn_ok = Button(window, text='OK', width=5, command=btn_ok_clicked)
btn_ok.grid(row=6, column=3, sticky=W)
btn_cancel = Button(window, text='Cancel', width=5, command=btn_cancel_clicked)
btn_cancel.grid(row=6, column=4, sticky=W)

### START PROGRAM ###
window.mainloop()