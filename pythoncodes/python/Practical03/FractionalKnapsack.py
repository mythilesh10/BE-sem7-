import time
start = time.time()

def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    item_value_ratio = [(item[1] / item[0], item) for item in items]
    
    # Sort items by value-to-weight ratio in descending order
    item_value_ratio.sort(reverse=True)
    
    total_value = 0  # Total value of selected items
    knapsack = []    # Items selected for the knapsack
    
    for value_per_weight, item in item_value_ratio:
        if capacity >= item[0]:  # If the item can fit entirely
            knapsack.append((item, 1))  # Add the whole item
            total_value += item[1]
            capacity -= item[0]
        else:  # If the item can only fit partially
            fraction = capacity / item[0]
            knapsack.append((item, fraction))  # Add a fraction of the item
            total_value += item[1] * fraction
            break  # The knapsack is now full
    
    return total_value, knapsack

# Example usage:
items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
capacity = 10
max_value, selected_items = fractional_knapsack(items, capacity)

print("Maximum value: {}".format(max_value))
print("Selected items:")
for item, fraction in selected_items:
    print("  {}: Fraction = {}".format(item,round(fraction,2)))

end = time.time()
print("\nExecution time is: {}ms".format((end-start)*10**3))