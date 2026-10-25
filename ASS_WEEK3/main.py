
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from hybrid import hybrid_merge_sort
from merge import merge_sort
from quickSort import quick_sort
from heap import heap_sort

from utlis import genrate_array, time_sort

sizes = [100, 1000, 10000, 25000]

algorithms = [
    ("bubble_sort", bubble_sort),
    ("selection_sort", selection_sort),
    ("insertion_sort", insertion_sort),
    ("hybrid_merge_sort", lambda arr: hybrid_merge_sort(arr, 10)),
    ("merge_sort", merge_sort),
    ("quick_sort", lambda arr: quick_sort(arr, 0, len(arr) - 1)),
    ("heap_sort", heap_sort)
]

results = {name: [] for name, _ in algorithms}

for size in sizes:
    data = genrate_array(size)

    for name, sort_function in algorithms:
        ms = time_sort(sort_function, data)
        results[name].append(ms)

        print(f"running time for {name}, {size}, Time: {ms} milliseconds")
