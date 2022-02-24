import serial
import re
import tkinter as tk
# root = tk.Tk()
# root.title("my title")
# root.geometry('800x450')
# root.configure(background='white')
# label = tk.Label(text="Hello, Tkinter")
# label = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black"  # Set the background color to black
# )
# root.mainloop()


    

print(serial.__version__)
ser = serial.Serial('/dev/cu.usbmodem1101', 9600,timeout=1)
l=[]
for i in range(0,13):
        # print(ser.readline().decode())
        
        l.append(ser.readline().decode())
ser.close()

print("===========List===========")
l=[x.replace("\r\n","") for x in l]
print(l)
from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=10,background='white')
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
Lb = Listbox(master)
print(l[5])
Lb.insert(1, l[3])
Lb.insert(2, l[4])
Lb.insert(3, l[5])
Lb.insert(4, l[6])
Lb.insert(5, l[7])
Lb.insert(6, l[8])
Lb.insert(7, l[9])
Lb.insert(8, l[10])
Lb.pack()
master.mainloop()
w.pack()
mainloop()

# master = Tk()
# master.title('Field Details')
# w = Canvas(master, width=40, height=60)

