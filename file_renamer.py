import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(file_paths, new_name):
    try:
        # Пройтись по каждому выбранному файлу и переименовать его
        for i, file_path in enumerate(file_paths, 1):
            # Получить имя файла из пути
            filename, file_extension = os.path.splitext(os.path.basename(file_path))
            
            # Получить путь к директории
            directory = os.path.dirname(file_path)
            
            # Сгенерировать новое имя файла с добавлением счетчика
            new_filename = f"{new_name}{i}{file_extension}"
            
            # Переименовать файл
            os.rename(file_path, os.path.join(directory, new_filename))
            print(f"Файл {filename} переименован в {new_filename}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при переименовании файлов: {e}")

def browse_files():
    try:
        # Открыть диалоговое окно для выбора файлов
        files = filedialog.askopenfilenames()
        return files
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при выборе файлов: {e}")

def submit():
    # Получить новое имя из поля ввода
    new_name = entry.get()
    
    if not new_name:
        messagebox.showerror("Ошибка", "Вы не ввели новое имя файла.")
        return
    
    # Получить выбранные файлы
    file_paths = browse_files()
    
    if not file_paths:
        messagebox.showerror("Ошибка", "Вы не выбрали файлы для переименования.")
        return
    
    # Переименовать выбранные файлы
    rename_files(file_paths, new_name)

# Создать графический интерфейс
root = tk.Tk()
root.title("Переименование файлов")
root.geometry("400x250")  # Установить размер окна
root.resizable(False, False)  # Запретить изменение размера окна

# Создать метку и поле для ввода нового имени
label = tk.Label(root, text="Введите новое имя:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack()

# Создать кнопку для выбора файлов и переименования
button = tk.Button(root, text="Выбрать файлы", command=submit)
button.pack(pady=20)

# Запустить основной цикл событий
root.mainloop()
