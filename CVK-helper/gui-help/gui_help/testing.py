from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
class MainWindow(Frame):
    def __init__(self):
        super().__init__()
        
        self.pack(expand=Y,fill=BOTH)
        
        self.outercanvas = Canvas(self, width=150, height=100, bg='dodger blue')
        self.outercanvas.pack(expand=Y,fill=BOTH)
        #img=PhotoImage(file=r'C:\Users\Satwik\Desktop\pnf.png')
        self.innercanvas = Canvas(self.outercanvas, width=50, height=50,bg='#ffff00')
        self.outercanvas.create_window(50, 25, anchor=NW, window=self.innercanvas)
        #self.outercanvas.create_image(0,0,anchor=NW,image=img,window=self.innercanvas)
        self.innercanvas.create_text(10, 10, anchor=NW, text="Hello")

root = MainWindow()
root.mainloop()
