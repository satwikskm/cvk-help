from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Annapurna')
outer_canvas=Canvas(root,width=500,height=500,bg='white')
outer_canvas.pack(expand=Y,fill=BOTH)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Satwik\\Desktop\\pnf.png"))
outer_canvas.create_image(10,10,anchor=NW,image=image)
innercanvas = Canvas(outer_canvas, width=200, height=200,bg='sky blue')
outer_canvas.create_window(10, 10, anchor=NW, window=innercanvas)
innercanvas.create_text((10, 10), anchor=NW, text="kaha kan kahucha")
outer_canvas.pack()
root.mainloop()