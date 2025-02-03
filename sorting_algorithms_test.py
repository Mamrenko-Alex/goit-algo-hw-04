import timeit
import random
import matplotlib.pyplot as plt

# Algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsort(arr):
    return sorted(arr)

# Measure time
def measure_time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr.copy()), number=1)

# Test data
sizes = [100, 1000, 5000, 10000, 50000, 100000, 1000000]
test_data = {}

for size in sizes:
    test_data[size] = [random.randint(0, 10000) for _ in range(size)]

# Measuring execution time
results = {}

for size, data in test_data.items():
    results[size] = {
        "Insertion Sort": measure_time(insertion_sort, data) if size <= 10000 else 'A very long time',
        "Merge Sort": measure_time(merge_sort, data),
        "Timsort": measure_time(timsort, data) 
    }

# Graph
fig, ax = plt.subplots()
sort_types = ["Insertion Sort", "Merge Sort", "Timsort"]
colors = ["red", "blue", "green"]

for algo, color in zip(sort_types, colors):
    times = [results[size][algo] for size in sizes]
    sizes_filtered = [size for size in sizes]
    ax.plot(sizes_filtered, times, marker='o', linestyle='-', color=color, label=algo)

ax.set_xlabel("Array Size")
ax.set_ylabel("Execution Time (seconds)")
ax.set_title("Sorting Algorithm Performance Comparison")
ax.legend()

# Results
for size, timings in results.items():
    print(f"Array size: {size}")
    for algo, time_taken in timings.items():
        print(f"    {algo}: {time_taken} seconds")
    print()

plt.show()
