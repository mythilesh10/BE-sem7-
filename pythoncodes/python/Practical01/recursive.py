import time
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = 10
print("Recursive Approach")
result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is {result}.")

#########################################################
# Recursive Approach with Execution Time
#########################################################

start = time.time()

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = 10
print("Recursive Approach with Execution Time")
result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is {result}.")

end = time.time()
print("Execution time is: {}ms".format((end-start)*10**3))

####################################################################################################
# Time Complexity (Recursive):
# The time complexity of this approach is exponential, O(2^n). This is because it recursively calls itself twice for each value of n, leading to a large number of repeated calculations.

# Space Complexity (Recursive):
# The space complexity is O(n) because it creates a recursive call stack of depth n. Each recursive call consumes space on the call stack until it reaches the base case and starts returning values.

# The non-recursive (iterative) approach is more efficient in terms of both time and space complexity compared to the recursive approach. The recursive approach has exponential time complexity and can become very slow for larger values of n. 
# Additionally, it may lead to a stack overflow error for large values of n due to the large number of recursive function calls.

# The non-recursive approach, on the other hand, has a linear time complexity and uses constant space, making it suitable for calculating Fibonacci numbers for larger values of n.
####################################################################################################

