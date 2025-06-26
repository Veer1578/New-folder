from tkinter import *

root = Tk()
root.title('Conversion Calculator')
root.geometry('400x400')

label = Label(text='Enter length in inches')
label.place(x=20, y=60)

inpt = Entry(root, width=15)
inpt.place(x=150, y=60)

converted = Label(root)
converted.place(x=90, y=120)

def display():
    inches = float(int(inpt.get()))
    cm = inches * 2.54
    converted.config(text='In cm it is ' + str(cm))

button = Button(text='Convert to centimeter', command=display)
button.place(x=250, y=60)

root.mainloop()