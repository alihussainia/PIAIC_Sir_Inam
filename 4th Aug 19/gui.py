# !/usr/bin/python3
from tkinter import *

top = Tk()
frame_1 = Frame(top)
L1 = Label(frame_1, text = "User Name")
#L1.pack()
L1.pack( side = LEFT)
E1 = Entry(frame_1, bd = 5)
#E1.pack()
E1.pack(side = RIGHT)
frame_2 = Frame(top)
label_2 = Label(frame_2, text="Password")
label_2.pack(side = LEFT)
entry_2 = Entry(frame_2, bd=5)
entry_2.pack(side = RIGHT)
frame_1.pack()
frame_2.pack()
top.mainloop()