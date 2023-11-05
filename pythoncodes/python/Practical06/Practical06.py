import random
import time

def deterministic_partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]
    return right

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(func, arr):
    start_time = time.time()
    func(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    array_size = 1000
    arr = generate_random_array(array_size)

    print("Deterministic Quick Sort:")
    det_time = measure_time(deterministic_quick_sort, arr.copy())
    print(f"Execution time: {det_time:.6f} seconds")

    arr = generate_random_array(array_size)

    print("\nRandomized Quick Sort:")
    rand_time = measure_time(randomized_quick_sort, arr.copy())
    print(f"Execution time: {rand_time:.6f} seconds")
