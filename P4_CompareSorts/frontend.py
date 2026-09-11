import tkinter as tk
import matplotlib.pyplot as plt
import benchmark as ga

def generate_graph():
    plt.figure(num="Grafica", clear=True)
    for indx, list_time in times.items():
        plt.plot(elements, list_time, marker='o', label=indx)
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución del algoritmo Bubble Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

def imprimir(arr):
    resultArea.config(text=str(arr))

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
maxArea = tk.Scale(root, from_=100, to=10000, orient=tk.HORIZONTAL, length=400)
maxArea.pack(pady=10)
array = []
elements = []
times = {}
btn = tk.Button(root, text="Generar", command=lambda: ga.generate_arrays(array, elements, int(minArea.get()), int(incArea.get()), int(maxArea.get())))
btn.pack(pady=10)

btn3 = tk.Button(root, text="Imprimir", command=lambda: imprimir(array))
btn3.pack(pady=10)

resultArea = tk.Label(root, text="")
resultArea.pack(pady=10)

btn2 = tk.Button(root, text="Ordenar", command=lambda: ga.TestBenchAll(array, times))
btn2.pack(pady=10)

orderedArea = tk.Label(root, text="")
orderedArea.pack(pady=10)

btn.graph = tk.Button(root, text="Generar Grafica", command=generate_graph)
btn.graph.pack(pady=10)


root.mainloop()
