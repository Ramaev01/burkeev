import csv
import copy
import config
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class MainApp(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.count = 2
        self.button1 = tk.Button(self,text="Выбрать файл",fg="black", bg="white", width=30, height=2, command=self.load_file).grid(row=1,column=0, padx=1, columnspan=3)
        self.button2 = tk.Button(self, text="Визуализация",fg="black", bg="white", width=30, height=2, command=self.new_window).grid(row=2,column=0, padx=1, pady=5)

    def new_window(self):
        self.app = GraphWindow()
        self.app.title("Окно визуализации")
        self.app.mainloop()

    def load_file(self, config=None):
        # Загрузка csv
        filepath = filedialog.askopenfilename()
        if filepath != "":
            from distutils.command.config import config
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

class GraphWindow(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.button3 = tk.Button(self, text="Построить Эпюру",fg="black", bg="white", width=30, height=2)
        self.data = np.array(config.data)
        self.point1 = None
        self.point2 = None
        self.point1Bool = True
        self.drawLine = None
        self.drawLineBool = False
        self.point1Scatter = None
        self.point2Scatter = None

        self.canvas = None
        if (self.data.shape[0] == 0):
            ErrorWindow(self, config.errorData)
        else:
            if (self.data.shape[1] != 3):
                ErrorWindow(self, config.errorDataImport)
            else:
                self.graph()

    def graph(self):
        fig = Figure(figsize=(5, 5),
                    dpi=100)
    # Добавление subplot
        self.plot1 = fig.add_subplot(111)
    # Изобразить scatter
        self.s = 10
        x = self.data[:, 0].flatten()
        y = self.data[:, 1].flatten()
        colors = [self.data[:, 2].flatten()]
        scatter = self.plot1.scatter(x, y, c=colors, s=self.s, cmap='viridis')
        # создать легенду с уникальными цветами из scatter
        legend1 = self.plot1.legend(*scatter.legend_elements(),
                                    loc="upper right", title="R")
        self.plot1.add_artist(legend1)
        # Создание Tkinter canvas
        # включение в нее Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig,
                                        master=self)
        self.canvas.draw()
        self.canvas.mpl_connect('button_press_event', self.onpick)
        # размещение the Tkinter window
        self.canvas.get_tk_widget().pack()
        # создание Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas,
                                       self)
        toolbar.update()
    # размещение toolbar в Tkinter window
        self.canvas.get_tk_widget().pack()


class ErrorWindow(Toplevel):

    def __init__(self, master, error_info, *args, **kwargs):
        super(ErrorWindow, self).__init__(master, *args, **kwargs)
        """
        Display code here
        """

def main():
    app = MainApp()
    app.title("Визуализация триангуляционных данных")
    app.mainloop()
if __name__ == '__main__':
    main()

