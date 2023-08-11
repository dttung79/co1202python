from tkinter import *
from tkinter.ttk import Combobox

student_names = ["John", "Mary", "Peter", "Jane", "Tom", "Alice"]
student_ids = ['GCH20012', 'GCH20013', 'GCH20014', 'GCH20015', 'GCH20016', 'GCH20017']
student_gpas = [8.0, 8.5, 6.5, 7.0, 9.0, 7.5]
### EVENT HANDLERS ###
def cbb_students_selected(event):
    # get selected index
    selected_index = cbb_students.current()
    if selected_index == -1: # no item selected
        return
    # update name
    name =student_names[selected_index]
    txt_name.delete(0, END)
    txt_name.insert(0, name)
    # update id
    id = student_ids[selected_index]
    txt_id.delete(0, END)
    txt_id.insert(0, id)
    # update gpa
    gpa = student_gpas[selected_index]
    txt_gpa.delete(0, END)
    txt_gpa.insert(0, gpa)
    
### CREATE WINDOW & WIDGETS ###
window = Tk()
window.title("Students Management")
window.geometry("500x200")

lbl_students = Label(window, text="Students")
lbl_students.grid(row=0, column=0, sticky=W, padx=10)

cbb_students = Combobox(window, width=20)
cbb_students["values"] = student_names
cbb_students.grid(row=1, column=0, sticky=W)
cbb_students.bind("<<ComboboxSelected>>", cbb_students_selected)

lbl_name = Label(window, text="Name")
lbl_name.grid(row=1, column=1, sticky=W)

txt_name = Entry(window, width=20)
txt_name.grid(row=1, column=2, sticky=W)

lbl_id = Label(window, text="ID")
lbl_id.grid(row=2, column=1, sticky=W)

txt_id = Entry(window, width=20)
txt_id.grid(row=2, column=2, sticky=W)

lbl_gpa = Label(window, text="GPA")
lbl_gpa.grid(row=3, column=1, sticky=W)

txt_gpa = Entry(window, width=20)
txt_gpa.grid(row=3, column=2, sticky=W)
### START PROGRAM ###
window.mainloop()