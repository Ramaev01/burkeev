from tkinter import *
room = Tk()
room.configure(bg="orange")
mylabel1 = Label(room, text="Hello world", fg="white", bg="#00BFFF", width=10, borderwidth=20).grid(row=0, column=0, pady=10, padx=10)
mylabel2 = Label(room, text="", fg="white", bg="#00BFFF", width=10, borderwidth=20).grid(row=0, column=5, pady=10, padx=10)
mylabel3 = Label(room, text="", fg="white", bg="#00BFFF", width=10, borderwidth=20).grid(row=1, column=0, pady=10, padx=10)
mylabel4 = Label(room, text="Меня зовут Рамиль", fg="white", bg="#00BFFF", width=10, borderwidth=20).grid(row=1, column=5, pady=10, padx=10)
room.mainloop()
