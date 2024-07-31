import tkinter as tk
from tkinter import messagebox

def agregar_nota():
    try:
        nota = float(entry_nota.get())
        notas.append(nota)
        entry_nota.delete(0, tk.END)
        lista_notas.insert(tk.END, nota)
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

def calcular_promedio():
    if notas:
        promedio = sum(notas) / len(notas)
        messagebox.showinfo("Promedio", f"El promedio de las notas es: {promedio:.2f}")
    else:
        messagebox.showinfo("Sin notas", "No se ingresaron notas.")


root = tk.Tk()
root.title("Calculadora de Promedio de Notas")

notas = []


entry_nota = tk.Entry(root, width=10)
entry_nota.pack(pady=5)


btn_agregar = tk.Button(root, text="Agregar Nota", command=agregar_nota)
btn_agregar.pack(pady=5)


lista_notas = tk.Listbox(root, width=20, height=10)
lista_notas.pack(pady=5)


btn_promedio = tk.Button(root, text="Calcular Promedio", command=calcular_promedio)
btn_promedio.pack(pady=5)

root.mainloop()
