import random
import tkinter as tk
import matplotlib.pyplot as plt
import time

def bubble_sort(arro):
    arr = arro.copy()
    start_time = time.perf_counter()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    times.append(execution_time)

def selection_sort(arro):
    arr = arro.copy()
    start_time = time.perf_counter()
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    times2.append(execution_time)
    return arr

def selection_sort_automatic(array):
    for i in array:
        selection_sort(i)
     
def bubble_sort_automatic(array):
    for i in array:
        bubble_sort(i)
    orderedArea.config(text="Arreglo Ordenado!!")

def generate_array(arr):
            arr.clear()
            times.clear()
            times2.clear()
            elements.clear()
            min_val = int(minArea.get())
            increment = int(incArea.get())
            max_val = int(maxArea.get())
            aux = []
            if max_val > min_val:
                for i in range(min_val, max_val+1, increment):
                    for j in range(i):
                        aux.append(random.randint(1, max_val*2))
        
                    arr.append(aux.copy())
                    aux.clear()
                    elements.append(i)
                resultArea.config(text=str(arr))
                #orderedArea.config(text="")
            else:
                print("Rango Invalido")

def bubble_sort_automatic(array):
    for i in array:
        bubble_sort(i)
    orderedArea.config(text="Arreglo Ordenado!!")

def generate_graph():
    plt.figure(num="Grafica", clear=True)
    plt.plot(elements, times, marker='o', label="BubbleSort")
    plt.plot(elements, times2, marker='o', label="SelectionSort")
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución del algoritmo Bubble Sort')
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("BubbleSort")
root.geometry("900x700")
minText = tk.Label(root, text="Ingresa el numero de elementos inicial")
minText.pack(pady=10)
#minArea = tk.Entry(root)
minArea = tk.Scale(root, from_=5, to=100, orient=tk.HORIZONTAL, length=200)
minArea.pack(pady=10)
incText = tk.Label(root, text="Ingresa cuanto se va a incrementar el numero de elementos: ")
incText.pack(pady=10)
incArea = tk.Scale(root, from_=5, to=100, orient=tk.HORIZONTAL, length=200)
incArea.pack(pady=10)
maxText = tk.Label(root, text="Ingresa el numero de elementos final: ")
maxText.pack(pady=10)
maxArea = tk.Scale(root, from_=1000, to=1000000, orient=tk.HORIZONTAL, length=200)
maxArea.pack(pady=10)
array = []
elements = []
times = []
times2 = []
btn = tk.Button(root, text="Generar", command=lambda: generate_array(array))
btn.pack(pady=10)

resultArea = tk.Label(root, text="")
resultArea.pack(pady=10)

btn2 = tk.Button(root, text="Ordenar", command=lambda: (bubble_sort_automatic(array), selection_sort_automatic(array)))
btn2.pack(pady=10)

orderedArea = tk.Label(root, text="")
orderedArea.pack(pady=10)

btn.graph = tk.Button(root, text="Generar Grafica", command=generate_graph)
btn.graph.pack(pady=10)


root.mainloop()
