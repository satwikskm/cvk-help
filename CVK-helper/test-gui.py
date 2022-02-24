from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=100,background='white')
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
Lb = Listbox(master)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
master.mainloop()
w.pack()
mainloop()