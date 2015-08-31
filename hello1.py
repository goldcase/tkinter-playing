#!/usr/bin/python
from Tkinter import *

# Initialize Tkinter by creating a Tk root widget.
root = Tk()

# Create a Label widget as a child to the root window
w = Label(root, text="Hello world")
# tells the size to fit the given text and make itself visible
w.pack()

root.mainloop()
