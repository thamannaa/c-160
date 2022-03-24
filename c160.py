from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("notepad")
root.minsize(650,650)
root.maxsize(650,650)


open_image=ImageTk.PhotoImage(Image.open("open.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))
exit_image=ImageTk.PhotoImage(Image.open("exit.jpg"))

label1=Label(root,text="File name")
label1.place(relx=0.28,rely=0.03,anchor=CENTER)

input_name=Entry(root)
input_name.place(relx=0.46,rely=0.03,anchor=CENTER)

text_1=Text(root,height=35,width=80)
text_1.place(relx=0.5,rely=0.55,anchor=CENTER)


root.mainloop()

