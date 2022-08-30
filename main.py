from socket import AI_NUMERICHOST
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
window=Tk()
window.geometry('800x800')
frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")
label1=Label(frame, text="WELCOME USER", font='Arial 17 bold')

label1.place(relx=0.5, rely=0.2, anchor=CENTER)
label2=Label(frame, text="SELECT THE OPTION", font='Arial 17 bold')
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
def clear():
    for widgets in frame.winfo_children():
      widgets.destroy()
def rotate():
    clear()
    
    def browseFiles():
        global filename,x
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        label_file_explorer.configure(text="File Opened: "+filename)
        x="there"
    def rotateright():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            img=Image.open(filename,"r")
            r_img=img.rotate(90)
            r_img.show()
    def rotateleft():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            img=Image.open(filename,"r")
            r_img=img.rotate(90)
            r_img.show()
    label1=Label(frame, text="select a file", font='Arial 17 bold')
    label1.place(relx=0.5, rely=0.2, anchor=CENTER)
    label_file_explorer = Label(frame, text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
    label_file_explorer.place(x=350,y=250)
    button_explore = Button(frame,text = "Browse Files",command = browseFiles)
    button_explore.place(x=350,y=300)
    rotateright= Button(frame,text = "rotate right",height=5,width=20,command = rotateright)
    rotateright.place(x=350,y=400)
    rotateleft = Button(frame,text = "rotate left",height=5,width=20,command = rotateleft)
    rotateleft.place(x=350,y=500)
def Changesize():
    clear()
    def browseFiles():
        global filename,x
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        label_file_explorer.configure(text="File Opened: "+filename)
        x="there"
    def resize():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            size=(int(entry1.get()),int(entry2.get()))
            img=Image.open(filename,"r")
            r_img=img.resize(size)
            r_img.show()
            r_img.save(filename)
     
    label_file_explorer = Label(frame, text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
    label_file_explorer.place(x=350,y=250)
    button_explore = Button(frame,text = "Browse Files",command = browseFiles)
    button_explore.place(x=350,y=300)
    firstsize=Label(text="enter the first size:",width=100,height=5)
    firstsize.place(x=350,y=400,anchor=CENTER)
    entry1=Entry(frame,text="enter the first size",bd=5)
    entry1.place(x=350,y=450,anchor=CENTER)
    secondsize=Label(text="enter the second  size:",width=100,height=5)
    secondsize.place(x=350,y=500,anchor=CENTER)
    entry2=Entry(frame,text="enter the second size",bd=5)
    entry2.place(x=350,y=550,anchor=CENTER)
    resize = Button(frame,text = "RESIZE",height=5,width=20,command = resize)
    resize.place(x=350,y=600)
def changetojpg():
    clear()
    
    def browseFiles():
        global filename,x
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        label_file_explorer.configure(text="File Opened: "+filename)
        x="there"
    def Convert():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            img=Image.open(filename,"r")
            rgb_im = img.convert("RGB")
            text=filename.split(".")
            rgb_im.save(text[0]+".jpg")

    label_file_explorer = Label(frame, text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
    label_file_explorer.place(x=350,y=250)
    button_explore = Button(frame,text = "Browse Files",command = browseFiles)
    button_explore.place(x=350,y=300)
    Convert= Button(frame,text = "CONVERT",height=5,width=20,command = Convert)
    Convert.place(x=350,y=600)
def changetopng():
    clear()
    
    def browseFiles():
        global filename,x
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        label_file_explorer.configure(text="File Opened: "+filename)
        x="there"
    def Convert():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            img=Image.open(filename,"r")
            text=filename.split(".")
            img.save(text[0]+".png")
    label_file_explorer = Label(frame, text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
    label_file_explorer.place(x=350,y=250)
    button_explore = Button(frame,text = "Browse Files",command = browseFiles)
    button_explore.place(x=350,y=300)
    Convert= Button(frame,text = "CONVERT",height=5,width=20,command = Convert)
    Convert.place(x=350,y=600)
def menuconvert():
    clear()
    button1=Button(frame,text="PNG TO JPG",height=5,width=20,command= changetojpg)
    button1.place(x=350,y=350,anchor=CENTER)
    button2=Button(frame,text="jpg to png",width=20,height=5,command=changetopng)
    button2.place(x=350,y=500,anchor=CENTER)
def resolutionchange():
    clear()
    def Convert():
        if x!="there":
            messagebox.showwarning("error", "NO FILE IS ADDED")
        else:
            global y
            y=int(entry2.get())
            img=Image.open(filename)
            img.save(filename,quality=y)
    def browseFiles():
        global filename,x
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        label_file_explorer.configure(text="File Opened: "+filename)
        x="there"
    label_file_explorer = Label(frame, text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
    label_file_explorer.place(x=350,y=250)
    button_explore = Button(frame,text = "Browse Files",command = browseFiles)
    button_explore.place(x=350,y=300)
    quality=Label(text="enter the quality",width=100,height=5)
    quality.place(x=350,y=400,anchor=CENTER)
    entry2=Entry(frame,text="ENTER THE QUALITY",bd=5)
    entry2.place(x=350,y=550,anchor=CENTER)
    Convert= Button(frame,text = "CONVERT",height=5,width=20,command = Convert)
    Convert.place(x=350,y=600)
rotate=Button(frame, text="rotate",height= 5, width=25,command=rotate)
rotate.place(x=350,y=300)
Changeresolution=Button(frame, text="change size",height=5, width=25,command=Changesize)
Changeresolution.place(x=350,y=400)
CHANGETOJPG=Button(frame, text="JPG TO PNG AND VICE VERSA",height=5, width=25,command=menuconvert)
CHANGETOJPG.place(x=350,y=500)
resize1=Button(frame, text="change resolution",height=5, width=25,command=resolutionchange)
resize1.place(x=350,y=600)
window.mainloop()