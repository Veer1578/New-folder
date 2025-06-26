from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Virus Scan')
root.geometry('200x200')

def detection():
    messagebox.askquestion('Alert', 'Stop! Virus found')

button = Button(root, text='Virus Scan', command=detection)
button.place(x=75, y=40)

root.mainloop()