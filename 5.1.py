from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


MainApp = Tk()
MainApp.title("Визуализация триангуляционных данных")

GraphWindow = Tk()
GraphWindow.title("Окно визуализации")

DiagramWindow = Tk()
DiagramWindow.title("Эпюра")

ErrorWindow = Tk()
ErrorWindow.title("Окно")

upload = Button(MainApp, text="Выбрать файл", fg="black", bg="white", width=30, height=2).grid(row=1,column=0, padx=1, columnspan=3)
vizualization = Button(MainApp, text="Визуализация", fg="black", bg="white", width=30, height=2).grid(row=2,column=0, padx=1, pady=5)

canva = Canvas(GraphWindow, width=600, height=400)
canva.pack()


def load_file(self):
    # Загрузка csv
    filepath = filedialog.askopenfilename()
    if filepath != "":
        config.data = []
        with open(filepath, encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Проверка количества и содержания столбцов
                    if len(row) != 3:
                        ErrorWindow(self, config.errorTextImport)
                        break
                else:
                    l = []
                    for num in row:
                        l.append(int(num))
                    config.data.append(l)
                count += 1
    else:
        ErrorWindow(self, config.errorTextImport)

MainApp.mainloop()
