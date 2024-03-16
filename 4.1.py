from tkinter import *
room = Tk()
def onclick():
    myLabel = Label(room, text = "Я нажал на кнопку!")
    myLabel.pack()

mybutton = Button(room, text = "Hello world", command = onclick, fg="white", bg="#00BFFF")
mybutton.pack()
room.mainloop()
