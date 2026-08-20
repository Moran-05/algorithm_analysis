def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_sort(array)
print("\n")
print("Lista Arreglada: ", array, "\n")
print("--------------------------------")