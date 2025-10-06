import tkinter as tk
from tkinter import messagebox
from mod9_core import neutral_nines_mod9

def calculate_mod9():
    try:
        number = int(entry.get())
        result = neutral_nines_mod9(number)
        messagebox.showinfo("Результат", f"Залишок по модулю 9 (без нейтральних): {result}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть ціле число!")

# Створення головного вікна
root = tk.Tk()
root.title("Правило нульового внеску в модулі 9")

# Розміри та стилізація
root.geometry("400x200")
root.configure(bg="#f0f0f0")

# Заголовок
title_label = tk.Label(root, text="Обчислення цифрового кореня", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Поле введення
entry_label = tk.Label(root, text="Введіть ціле число:", font=("Arial", 12), bg="#f0f0f0")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 12), width=20, justify="center")
entry.pack(pady=5)

# Кнопка обчислення
button = tk.Button(root, text="Обчислити", font=("Arial", 12), command=calculate_mod9, bg="#4CAF50", fg="white")
button.pack(pady=10)

# Запуск GUI
root.mainloop()
