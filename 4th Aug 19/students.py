from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.adamjee_students

entry_name = None
entry_fname = None

root = Tk()

def search_students():
    students = db.student.find()
    #print(students)
    data = ''
    for st in students:
        print('Here-1')
        print(st)
        data += 'Name: ' + st['Name'] + ' Father Name: ' + st['Father_Name']
        if 'Class' in st:
            data += ' Class: ' + st['Class']
        data += '\n'
    messagebox.showwarning('Students', data)

def save_student():
    student = {
        'Name': entry_name.get(),
        'Father_Name': entry_fname.get()
    }
    student_saved = db.student.insert_one(student)
    print(student_saved)

frame_1 = Frame(root)
lbl_name = Label(frame_1, text='Student Name')
lbl_name.pack(side=LEFT)
entry_name = Entry(frame_1, bd=5)
entry_name.pack(side=RIGHT)

frame_2 = Frame(root)
lbl_fname = Label(frame_2, text='Father Name')
lbl_fname.pack(side=LEFT)
entry_fname = Entry(frame_2, bd=5)
entry_fname.pack(side=RIGHT)
b1 = Button(root, text='Save', command=save_student)
b2 = Button(root, text='Search', command=search_students)
frame_1.pack()
frame_2.pack()
b1.pack()
b2.pack()
root.mainloop()