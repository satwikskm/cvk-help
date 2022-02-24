from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
root=Tk()
outercanvas = Canvas(root, width=150, height=100, bg='dodger blue')
outercanvas.pack(expand=Y,fill=BOTH)
img=PhotoImage(file=r'C:\Users\Satwik\Desktop\pnf.png')
innercanvas = Canvas(outercanvas, width=50, height=50,bg='#ffff00')
outercanvas.create_window(50, 25, anchor=NW, window=innercanvas)
#outercanvas.create_image(0,0,anchor=NW,image=img,window=innercanvas)
innercanvas.create_text(10, 10, anchor=NW, text="Hello")

root.mainloop()