import random
import sorts
import time

def generate_arrays(arr, elements, min_val, increment, max_val):
    arr.clear()
    elements.clear()
    if max_val > min_val:
        for i in range(min_val, max_val+1, increment):
            arr.append(generate_array(i, max_val))
            elements.append(i)
    else:
        print("Rango Invalido")

def generate_array(i, max_val):
    aux = []
    for j in range(i):
        aux.append(random.randint(1, max_val*2))
    return aux

def insertion_sort_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.insertion_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def gnome_sort_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.gnome_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def stooge_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.stooge_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def exchange_sort_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.exchange_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def selection_sort_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.selection_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times
     
def bubble_sort_automatic(array):
    times = []
    for i in array:
        start_time = time.perf_counter()
        sorts.bubble_sort(i)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times

def TestBenchAll(arr, times):
    times.update({"Insertion_sort" : insertion_sort_automatic(arr)})
    times.update({"gnome_sort" : gnome_sort_automatic(arr)})
    #times.update({"stooge_sort" : stooge_automatic(arr)})
    times.update({"exchange_sort" : exchange_sort_automatic(arr)})
    times.update({"bubble_sort" : bubble_sort_automatic(arr)})
    times.update({"selection_sort" : selection_sort_automatic(arr)})