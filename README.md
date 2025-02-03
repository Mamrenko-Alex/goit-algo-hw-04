# Sorting Algorithms Performance Analysis

## Overview

This project compares the performance of three sorting algorithms:

- **Insertion Sort**
- **Merge Sort**
- **Timsort** (built-in `sorted()` function in Python)

The execution time of each algorithm was measured using different dataset sizes, and the results were visualized using graphs.

## Results

### Observations:

- **Insertion Sort** performs well on small datasets but becomes inefficient for larger datasets due to its O(n²) complexity.
- **Merge Sort** shows better efficiency for larger datasets with O(n log n) complexity but has higher memory usage due to recursive calls.
- **Timsort** consistently outperforms both algorithms, especially on larger datasets, due to its hybrid approach combining merge sort and insertion sort.

### Performance Comparison:

| Array Size | Insertion Sort (s)    | Merge Sort (s) | Timsort (s) |
| ---------- | --------------------- | -------------- | ----------- |
| 100        | Fast                  | Fast           | Very Fast   |
| 1000       | Fast                  | Moderate       | Fast        |
| 5000       | Slow                  | Slower         | Very Fast   |
| 10000      | Slower                | Slowest        | Very Fast   |
| 50000      | Slowest               | Slowest        | Very Fast   |
| 100000     | Impossible to measure | Slowest        | Very Fast   |
| 1000000    | Impossible to measure | Slowest        | Very Fast   |

## Visualization

Below is a graphical representation of the performance of each sorting algorithm:

![Sorting Performance Graph](/data.jpg)

_(Replace `path/to/your/screenshot.png` with the actual path to your screenshot.)_

## Instructions to Run the Experiment

To reproduce the experiment on your computer, follow these steps:

### Prerequisites

Ensure you have Python installed. You also need the following libraries:

```sh
pip install matplotlib
```

### Running the Experiment

1. Clone this repository or download the script.
2. Navigate to the script directory.
3. Run the script using:

```sh
python sorting_algorithms_test.py
```

This will generate the performance comparison graph and output execution times in the console.

## Conclusion

Timsort is the most efficient algorithm among the three, making it the preferred choice for sorting in Python. It optimally combines insertion sort for small partitions and merge sort for larger partitions, ensuring stable and fast performance.

Programmers typically rely on Python's built-in sorting functions (`sorted()` and `.sort()`) instead of implementing sorting algorithms from scratch, as they are optimized for real-world applications.

## Future Improvements

- Extend the comparison to additional sorting algorithms like QuickSort or HeapSort.
- Analyze memory consumption alongside execution time.
- Test on nearly sorted or reversed datasets to evaluate algorithm adaptability.
