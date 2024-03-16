from tkinter import *
room = Tk()

e = Entry(room, width=50, fg="white", bg="#00BFFF", borderwidth=5)
e.pack()
e.insert(0, "Введите ваше имя: ")
def onClick():
    hello = "Привет, " + e.get()
    mylabel = Label(room, text=hello)
    mylabel.pack()

mybutton = Button(room, text="Нажмите", command=onClick, fg="blue", bg="white")
mybutton.pack()
room.mainloop()