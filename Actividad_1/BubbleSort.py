import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_array(arr):
    cycle = 1
    while cycle == 1:
            min = int(input("Ingresa el numero de elementos inicial: "))
            increment = int(input("Ingresa cuanto se va a incrementar el numero de elementos: "))
            max = int(input("Ingresa el numero de elementos final: "))
            aux = []
            if max > min:
                for i in range(min, max+1, increment):
                    for j in range(i):
                        aux.append(random.randint(1, max))
        
                    arr.append(aux.copy())
                    aux.clear()
                cycle = 0
            else:
                print("Rango Invalido")

array = []
generate_array(array)
#bubble_sort(array)
print("\n")
print("Lista Arreglada: ", array, "\n")
print("--------------------------------")