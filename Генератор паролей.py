import tkinter as tk
from tkinter import ttk, filedialog
import string
import random

# Функция для генерации пароля
def generate_password(length, use_digits, use_punctuation, use_letters):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if use_letters:
        characters += string.ascii_letters
    if characters:
        return ''.join(random.choice(characters) for _ in range(length))
    else:
        return ''

# Команда для кнопки генерации
def on_generate_clicked():
    length = int(length_var.get())
    use_digits = digits_var.get()
    use_punctuation = punctuation_var.get()
    use_letters = letters_var.get()
    password = generate_password(length, use_digits, use_punctuation, use_letters)
    password_var.set(password)

# Функция для сохранения пароля в файл
def save_password():
    password = password_var.get()
    if password:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(password)
                tk.messagebox.showinfo("Генератор паролей", "Пароль успешно сохранен!")
    else:
        tk.messagebox.showwarning("Генератор паролей", "Сначала сгенерируйте пароль!")

# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")

# Создание и расположение виджетов
length_var = tk.StringVar(value='12')
digits_var = tk.BooleanVar(value=True)
punctuation_var = tk.BooleanVar(value=True)
letters_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

ttk.Label(root, text="Длина пароля:").grid(column=0, row=0, sticky=tk.W)
ttk.Entry(root, textvariable=length_var).grid(column=1, row=0)

ttk.Checkbutton(root, text="Использовать цифры", variable=digits_var).grid(column=0, row=1, sticky=tk.W)
ttk.Checkbutton(root, text="Использовать символы", variable=punctuation_var).grid(column=0, row=2, sticky=tk.W)
ttk.Checkbutton(root, text="Использовать буквы", variable=letters_var).grid(column=0, row=3, sticky=tk.W)

ttk.Button(root, text="Сгенерировать пароль", command=on_generate_clicked).grid(column=0, row=4, columnspan=2, pady=5)

ttk.Entry(root, textvariable=password_var, state='readonly').grid(column=0, row=5, columnspan=2, sticky=tk.EW)

ttk.Button(root, text="Сохранить пароль", command=save_password).grid(column=0, row=6, columnspan=2, pady=5)

# Запуск главного цикла
root.mainloop()

