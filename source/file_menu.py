from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys

class File():
    def newFile(self):
        self.filename = "Untitled"
        self.text.delete(0.0, END)

    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Oops!", message="Unable to save file...")

    def saveFile(self):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename,'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def openFile(self):
        f = askopenfile(mode="r+")
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, END)


    def quit(self):
        entry = askyesno(title="Quit", message="Are you sure to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root

def main(root, textbox, menubar):

    file_menu = Menu(menubar, tearoff=False)
    fileObject = File(textbox, root)

    file_menu.add_command(label="New", command=fileObject.newFile, accelerator="")
    file_menu.add_command(label="Open", command=fileObject.openFile, accelerator="")
    file_menu.add_command(label="Save", command=fileObject.saveAs, accelerator="")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=fileObject.quit, accelerator="Ctrl+Q")
    menubar.add_cascade(label="File", menu=file_menu)

    #root.bind_all("<Control-s>", fileObject.saveFile)
    #root.bind_all("<Control-q>", fileObject.quit)
    root.config(menu=menubar)


