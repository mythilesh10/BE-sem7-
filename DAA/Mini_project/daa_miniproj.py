import numpy as np
import threading
import time

# Function for normal matrix multiplication
def matrix_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Function for multithreaded matrix multiplication (one thread per row)
def threaded_matrix_multiply_row(matrix1, matrix2):
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    threads = []
    for i in range(matrix1.shape[0]):
        thread = threading.Thread(target=calculate_row, args=(matrix1, matrix2, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

def calculate_row(matrix1, matrix2, result, i):
    for j in range(matrix2.shape[1]):
        result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))

# Function for multithreaded matrix multiplication (one thread per cell)
def threaded_matrix_multiply_cell(matrix1, matrix2):
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    threads = []
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            thread = threading.Thread(target=calculate_cell, args=(matrix1, matrix2, result, i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result

def calculate_cell(matrix1, matrix2, result, i, j):
    result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))

# Get dynamic input for matrix dimensions
m, n, p = map(int, input("Enter dimensions of the first matrix (m x n): ").split())
q, r, s = map(int, input("Enter dimensions of the second matrix (q x r): ").split())

# Generate random matrices based on input dimensions
matrix1 = np.random.rand(m, n)
matrix2 = np.random.rand(q, r)

start_time = time.time()
result_normal = matrix_multiply(matrix1, matrix2)
end_time = time.time()
print("Time for normal matrix multiplication:", end_time - start_time)
print("Result of normal matrix multiplication:\n", result_normal)

start_time = time.time()
result_threaded_row = threaded_matrix_multiply_row(matrix1, matrix2)
end_time = time.time()
print("Time for threaded matrix multiplication (one thread per row):", end_time - start_time)
print("Result of threaded matrix multiplication (one thread per row):\n", result_threaded_row)

start_time = time.time()
result_threaded_cell = threaded_matrix_multiply_cell(matrix1, matrix2)
end_time = time.time()
print("Time for threaded matrix multiplication (one thread per cell):", end_time - start_time)
print("Result of threaded matrix multiplication (one thread per cell):\n", result_threaded_cell)
