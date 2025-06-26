from tkinter import *

root = Tk()
root.title('Event Handler')
root.geometry('100x100')


def key_pressed(event):
    '''Print the character associated to the key press'''
    print(event.char)


root.bind('<Key>', key_pressed)


def button_pressed(event):
    '''Print the character associated to the key press'''
    print('The button was clicked')


buttn = Button(text='Click Me')
buttn.pack()


root.bind('<Button-1>', button_pressed)

root.mainloop()
