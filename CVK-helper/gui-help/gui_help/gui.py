from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import serial
import re
#image=ImageTk.PhotoImage(Image.open("C:\\Users\\Satwik\\Desktop\\pnf.png"))
ser = serial.Serial('/dev/cu.usbmodem1101', 9600,timeout=1)
l=[]
for i in range(0,13):
        # print(ser.readline().decode())
        
        l.append(ser.readline().decode())
ser.close()
l=[x.replace("\r\n","") for x in l]
class Display:
    "this will render the display of the touch screen"

    def __init__(self):
        #self.width  = 835
        self.width  = 1290
        #self.image=ImageTk.PhotoImage(Image.open("C:\\Users\\Satwik\\Desktop\\pnf.png"))
        #self.image=Image.open(r"C:\\Users\\Satwik\\Desktop\\pnf.png")
        #self.img=ImageTk.PhotoImage(file='C:\\Users\\Satwik\\Desktop\\pnf.png')
        #self.img=plt.imread("C:\\Users\\Satwik\\Desktop\\pnf.png")
        #self.image=cv2.imread("C:\\Users\\Satwik\\Desktop\\pnf.png")
        #self.height = 472
        self.height = 723
        self.window = Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("Anapurna")
        self.top_canvas = Canvas(self.window, width=self.width, height=127, bg="Red")
        #pic=PhotoImage(file=r'')
        #picimage = pic.subsample(13,13)
        #self.top_canvas.create_image(20,0,anchor=NW,image=picimage)
        #self.x_cord = 782
        #self.y_cord=10
        #self.status_box = self.top_canvas.create_rectangle(self.x_cord,self.y_cord,self.x_cord+45,self.y_cord+45, fill="blue")
        self.top_cavas_decoration()
        self.left_canvas = Canvas(self.window, width=self.width*0.75, height=565, bg="Pink")
        self.left_canvas_decoration()
        self.right_canvas = Canvas(self.window, width=self.width - self.width*0.75, height=565, bg="black")
        #self.right_canvas.create_image(10,10,anchor=NW,image=image)
        #photo = PhotoImage(file = r"C:\\Users\\Satwik\\Desktop\\pnf.png") 
        #photoimage = photo.subsample(3, 3)
        #self.left_canvas.create_image(240,10,anchor=NW,image=photoimage)
        self.right_canvas_decoration()
        self.run()
        
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)
        
    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
    
    def top_cavas_decoration(self):
        "this will perform the top canvas decoration and all required task"
        self.top_canvas.grid(row=0, column=0, columnspan=2, sticky=N)
        #self.app_name = self.top_canvas.create_text( (220,30),text="Annapurna", font=("Arial Bold",30))
        self.app_name = self.top_canvas.create_text( (550,50),text="Annapurna", font=("Calibri",100), fill="white")
                                                    
    def right_canvas_decoration(self):
        "this will perform the right canvas decoration and all required task"
        #img=PhotoImage(file='C:\\Users\\Satwik\\Desktop\\pnf.png')
        self.right_canvas.grid(row=1, column=1, rowspan=1, sticky=E)
        
    def left_canvas_decoration(self):
        "this will perform the left canvas decoration and all required task"
        self.left_canvas.grid(row=1, column=0, rowspan=1, sticky=W)
        self.app_name = self.left_canvas.create_text( (300,20),text=l[3], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (302,60),text=l[4], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,95),text=l[5], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,125),text=l[6], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,155),text=l[7], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,185),text=l[8], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,215),text=l[9], font=("Calibri",20), fill="Black")
        self.app_name = self.left_canvas.create_text( (300,245),text=l[10], font=("Calibri",20), fill="Black")


        
        # Lb = Listbox(self)
        # print(l[5])
        # Lb.insert(1, l[3])
        # Lb.insert(2, l[4])
        # Lb.insert(3, l[5])
        # Lb.insert(4, l[6])
        # Lb.insert(5, l[7])
        # Lb.insert(6, l[8])
        # Lb.insert(7, l[9])
        # Lb.insert(8, l[10])
        # Lb.pack()
        

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    d = Display()