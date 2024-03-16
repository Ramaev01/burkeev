from tkinter import *
room = Tk()
room.title("Калькулятор")
input_text = StringVar()
expression = ""

e = Entry(room, width=50, fg="black", bg="white", borderwidth=5).grid(row=0, column=0, columnspan=4)

def button_click(number):
    global expression
    second = expression + str(number)
    input_text.set(second)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


#первая строка
clear = Button(room, text="Очистить", fg="black", bg="white", width=30, height=2, command = lambda: bt_clear()).grid(row=1,column=0, padx=1, columnspan=3)
delenie = Button(room, text="/", fg="black", bg="white", width=8, height=2, command = lambda: button_click("/")).grid(row=1,column=3, padx=1, pady=5)

#вторая строка
seven = Button(room, text="7",fg="black", bg="white", width=8, height=2, command = lambda: button_click(7)).grid(row=2,column=0, padx=1, pady=5)
eight = Button(room, text="8",fg="black", bg="white", width=8, height=2, command = lambda: button_click(8)).grid(row=2,column=1, padx=1, pady=5)
nine = Button(room, text="9",fg="black", bg="white", width=8, height=2, command = lambda: button_click(9)).grid(row=2,column=2, padx=1, pady=5)
multiply = Button(room, text="*",fg="black", bg="white", width=8, height=2, command = lambda: button_click("*")).grid(row=2,column=3, padx=1, pady=5)

#третья строка
four = Button(room, text="4",fg="black", bg="white", width=8, height=2, command = lambda: button_click(4)).grid(row=3,column=0, padx=1, pady=5)
five = Button(room, text="5",fg="black", bg="white", width=8, height=2, command = lambda: button_click(5)).grid(row=3,column=1, padx=1, pady=5)
six = Button(room, text="6",fg="black", bg="white", width=8, height=2, command = lambda: button_click(6)).grid(row=3,column=2, padx=1, pady=5)
subtract = Button(room, text="-",fg="black", bg="white", width=8, height=2, command = lambda: button_click("-")).grid(row=3,column=3, padx=1, pady=5)

#Четвертая строка
one = Button(room, text="1",fg="black", bg="white", width=8, height=2, command = lambda: button_click(1)).grid(row=4,column=0, padx=1, pady=5)
two = Button(room, text="2",fg="black", bg="white", width=8, height=2, command = lambda: button_click(2)).grid(row=4,column=1, padx=1, pady=5)
three = Button(room, text="3",fg="black", bg="white", width=8, height=2, command = lambda: button_click(3)).grid(row=4,column=2, padx=1, pady=5)
add = Button(room, text="+",fg="black", bg="white", width=8, height=2, command = lambda: button_click("+")).grid(row=4,column=3, padx=1, pady=5)

#Пятая строка
zero = Button(room, text="0", fg="black", bg="white", width=30, height=2, command = lambda: button_click(0)).grid(row=5,column=0, padx=1, columnspan=3)
equal = Button(room, text="=", fg="black", bg="white", width=8, height=2, command = lambda: bt_equal()).grid(row=5,column=3, padx=1, pady=5)

room.mainloop()