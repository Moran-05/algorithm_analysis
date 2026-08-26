import tkinter as tk

def saludar():
    nombre = txtarea.get().strip()
    if not nombre:
        nombre = "Mundo"
    lbl.config(text=f"Hola, {nombre}")

root = tk.Tk()
root.title("Saludador de Compas")
root.geometry("400x300")

lbl = tk.Label(root, text="Hola, Escribe tu Nombre y presiona el boton", foreground="red")
lbl.pack(pady=10)

txtarea = tk.Entry(root)
txtarea.pack(pady=10)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

root.mainloop()