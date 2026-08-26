import random
import tkinter as tk

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_array(arr):
            min = int(minArea.get())#int(input("Ingresa el numero de elementos inicial: "))
            increment = int(incArea.get())#int(input("Ingresa cuanto se va a incrementar el numero de elementos: "))
            max = int(maxArea.get())#int(input("Ingresa el numero de elementos final: "))
            aux = []
            if max > min:
                for i in range(min, max+1, increment):
                    for j in range(i):
                        aux.append(random.randint(1, max))
        
                    arr.append(aux.copy())
                    aux.clear()
                resultArea.config(text=str(arr))
            else:
                print("Rango Invalido")

root = tk.Tk()
root.title("BubbleSort")
root.geometry("400x300")
minText = tk.Label(root, text="Ingresa el numero de elementos inicial")
minText.pack(pady=10)
minArea = tk.Entry(root)
minArea.pack(pady=10)
incText = tk.Label(root, text="Ingresa cuanto se va a incrementar el numero de elementos: ")
incText.pack(pady=10)
incArea = tk.Entry(root)
incArea.pack(pady=10)
maxText = tk.Label(root, text="Ingresa el numero de elementos final: ")
maxText.pack(pady=10)
maxArea = tk.Entry(root)
maxArea.pack(pady=10)
array = []
btn = tk.Button(root, text="Generar", command=lambda: generate_array(array))
btn.pack(pady=10)

resultArea = tk.Label(root, text="")
resultArea.pack(pady=10)

#array = []
#generate_array(array)
#bubble_sort(array)
print("\n")
print("Lista Arreglada: ", array, "\n")
print("--------------------------------")

root.mainloop()