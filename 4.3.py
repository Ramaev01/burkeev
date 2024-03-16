from tkinter import *
room = Tk()
def onclick():
    myLabel = Label(room, text = "Нажата кнопка!")
    myLabel.pack()

mybutton = Button(room, text="Нажмите", command=onclick, fg="blue", bg="white")
mybutton.pack()
room.mainloop()