from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("About Notepad", "Hello Everyone,\nThis is a simple working notepad\nWhich is devoloped by- PythonWithManan\nYou can do sevral things in it\nwrite anything you want.\nThankYou,\nManan Maheshwari[Devoloper]")

if __name__ == '__main__':
    """
    Basic Of Tkinter (Doing Setup of GUI)
    """
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("G:\\Python-Manan\\python-GUI(tkinter)\\Images\\logo.ico")
    root.geometry("544x544")

    
    # Adding Text to my Notepad
    global TextArea
    TextArea = Text(root, font="comicsansMS 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    """
    Creating Menu and Submenues for GUI
    #Flie Menu starts
    """
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    #Opening New File
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    root.config(menu=MenuBar)

    """
    Creating Menu and Submenues for GUI
    #Edit Menu starts
    """
    EditMenu = Menu(MenuBar, tearoff=0)

    #Giving features of [cut-copy-paste]-To our GUI
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    """
    Creating Menu and Submenues for GUI
    #Help Menu starts
    """
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    """
    Adding scrollbar to our GUI.
    For scrolling if text is more than the height of it.
    """
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()