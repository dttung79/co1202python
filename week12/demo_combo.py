from tkinter import *
from tkinter.ttk import Combobox

### EVENT HANDLERS ###
def cbb_languages_selected(event):
    # clear old text
    txt_language.delete(0, END)
    # insert new text (selected value from combobox)
    txt_language.insert(0, cbb_languages.get())

### CREATE WINDOW & WIDGETS ###
window = Tk()
window.title("Demo combobox")
window.geometry("300x200")

cbb_languages = Combobox(window, width=20)
cbb_languages["values"] = ("Python", "Java", "C#", "C++", "C", "JavaScript")
cbb_languages.grid(row=0, column=0)
cbb_languages.bind("<<ComboboxSelected>>", cbb_languages_selected)

txt_language = Entry(window, width=20)
txt_language.grid(row=0, column=1)


### START PROGRAM ###
window.mainloop()