import random
import time

def genrate_array(size):
    return [random.randint(1, size * 10) for _ in range(size)]

def time_sort(sort_function, original):
    arr = original.copy()
    start_time = time.time() #records the current time 
    sort_function(arr)
    end_time = time.time() #records time again
    return round((end_time - start_time) * 1000,2)  # Return time in milliseconds