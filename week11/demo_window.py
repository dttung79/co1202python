from tkinter import *
from tkinter import messagebox

# define a function to be called when the button OK is clicked
def btn_OK_clicked():
    messagebox.showinfo('Hello', 'Hello Python!')

window = Tk() # create a window
window.title("Hello GUI") # set the title of the window
window.geometry('500x300') # set the size of the window

lbl_hello = Label(window, text="Hello World!") # create a label
lbl_hello.grid(column=0, row=0) # place the label in the window

lbl_python = Label(window, text="I love Python!") # create a label
lbl_python.grid(column=1, row=1) # place the label in the window

# create a button, register a callback function to the button (or event handler)
btn_OK = Button(window, text="OK", command=btn_OK_clicked) 
btn_OK.grid(column=2, row=2) # place the button in the window

window.mainloop() # create an event loop listening to events