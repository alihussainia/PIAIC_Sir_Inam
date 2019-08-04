from tkinter import *
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['adamjee_students']

root = Tk()

entry_search = None
entry_new_fname = None
entry_new_name = None
txt_name_var = StringVar()
txt_fname_var = StringVar()

def remove_student():
    student_name = entry_search.get()
    db.student.remove({'Name': student_name})

def search():
    student_name = entry_search.get()
    student = db.student.find_one({'Name': student_name})
    txt_fname_var.set(student['Father_Name'])
    txt_name_var.set(student['Name'])

def update_student():
    student_name = entry_search.get()
    name = entry_new_name.get()
    fname = entry_new_fname.get()
    db.student.update_one(
        {'Name': student_name}, 
        {'$set': {'Class': 'AI'}}
    )

frame_1 = Frame(root)
label_1 = Label(frame_1, text='Search')
entry_search = Entry(frame_1, bd=5)

btn_search = Button(frame_1, text='Search', command=search)

entry_new_name = Entry(root, textvariable=txt_name_var)
entry_new_fname = Entry(root, textvariable=txt_fname_var)
btn_modify = Button(root, text='Update', command=update_student)
btn_delete = Button(root, text='Delete', command=remove_student)

label_1.pack(side=LEFT)
entry_search.pack(side=LEFT)
btn_search.pack(side=LEFT)

frame_1.pack()
entry_new_name.pack()
entry_new_fname.pack()
btn_modify.pack()
btn_delete.pack()  

root.mainloop()