from tkinter import *
from tkinter import messagebox


### EVENT HANDLERS ###
def lst_colors_selected(event):
    btn_choose_clicked()

def btn_choose_clicked():
    selected_index = lst_colors.curselection()
    if len(selected_index) == 0:
        messagebox.showerror('Index Error', 'Please choose a color')
        return
    selected_color = lst_colors.get(selected_index)
    # change background color of window
    window.configure(bg=selected_color)

### CREATE WINDOW & WIDGETS ###
window = Tk()
window.title("Demo listbox")
window.geometry("300x200")

lst_colors = Listbox(window, width=20, height=5, selectmode=SINGLE)
lst_colors.insert(1, "Red")
lst_colors.insert(2, "Green")
lst_colors.insert(3, "Blue")
lst_colors.insert(4, "Yellow")

lst_colors.grid(row=0, column=0)
lst_colors.bind("<<ListboxSelect>>", lst_colors_selected)

btn_choose = Button(window, text="Choose", command=btn_choose_clicked)
btn_choose.grid(row=1, column=0)

### START PROGRAM ###
window.mainloop()