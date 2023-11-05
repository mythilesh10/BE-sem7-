import time
start = time.time()

def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    
    # Create a table to store the maximum values for different capacities
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the table using dynamic programming
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the items included in the knapsack
    items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            items.append(i - 1)
            j -= weights[i - 1]
        i -= 1
    
    items.reverse()
    return dp[n][capacity], items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_dynamic_programming(values, weights, capacity)
print("Maximum Value: {}".format(max_value))
print("Selected Items: {}".format(selected_items))

end = time.time()
print("\nExecution time is: {}ms".format((end-start)*10**3))