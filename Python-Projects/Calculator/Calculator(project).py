from tkinter import *

"""
Function For Geting The Vakue Of The Button
"""
def click(event):
    global scvalue
    text = event.widget.cget("text")
    """
    Checking text value [1 value - " = ", 2 value - " c ", 3 value - any number.]
    """
    if text== "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    #Clearing our window
    if text== "Clear":
        scvalue.set("")
        screen.update()

    #Printing number to our window
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
root = Tk()
root.geometry("333x600")
root.config(bg="dark blue")
root.title("PythonWithManan - Calculator")
root.wm_iconbitmap("G:\\My apps Logos\\logo-calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="comicsansMS 30")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

"""
9 - 8 - 7 numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="9", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="8", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="7", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()

"""
6 - 5 - 4 numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="6", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="5", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="4", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()

"""
3 - 2 - 1 numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="3", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="2", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="1", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()

"""
0 - " - " - "  * " numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="0", padx=2.1,  font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="-", padx=5, font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="*", padx=2, font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()

"""
/ - % - = numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="/", padx=6,  font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="+", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="=",pady=6, font="lucida 26 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()

"""
c - 8 - 7 numbers
"""
frame = Frame(root, bg="dark blue")

button = Button(frame, text="Clear", font="lucida 30 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text=".",pady=6, font="lucida 26 bold", bg="orange")
button.pack(side=LEFT, padx=8, pady=5)
button.bind("<Button-1>", click)

frame.pack()
root.mainloop()
