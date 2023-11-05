def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
n = 10
print("Non Recursive Approch with Execution Time: ")
result = fibonacci_iterative(n)
print(f"The {n}th Fibonacci number is {result}.")


#############################################################################
# Non Recursive Approch with Execution Time
#############################################################################

import time

start = time.time()

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
n = 1000 # Use your own N
result = fibonacci_iterative(n)
print("Non Recursive Approch with Execution Time: ")
print(f"The {n}th Fibonacci number is {result}.")

end = time.time()
print("Execution time is: {}ms".format((end-start)*10**3))