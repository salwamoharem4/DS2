
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from utils import genrate_array, time_sort

sizes=[100,500,1000,2000] #different array sizes to test
algorithms=[("bubble_sort", bubble_sort), ("selection_sort", selection_sort) , ("insertion_sort", insertion_sort)] #list bakhazen feeha esm el algorithm bel function
results={name :[] for name, _ in algorithms}


for size in sizes:
    data = genrate_array(size)
    for name, sort_function in algorithms:
        ms=time_sort(sort_function, data) #mesure the execution time
        results[name].append(ms) #ba-add el mesured time lel list
        print(f"running time for {name} ,{size}, Time: {ms} milliseconds")

