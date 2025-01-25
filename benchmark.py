import time
import numpy as np
from randomized_quicksort import randomized_quicksort
from determinstic_quicksort import deterministic_quicksort

sizes = [10, 100, 1000, 10000]
results = {"randomized_quick_sort": [], "deterministic_quick_sort": []}

for size in sizes:
    array = np.random.randint(0, 1000, size).tolist()
    start = time.time()
    randomized_quicksort(array[:], 0, len(array) - 1)
    results["randomized_quick_sort"].append(time.time() - start)

    start = time.time()
    deterministic_quicksort(array[:], 0, len(array) - 1)
    results["deterministic_quick_sort"].append(time.time() - start)

print("Comparing runtime ", results)
