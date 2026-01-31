def fractional_knapsack(items, capacity):
    items = [(v, w, v/w) for v, w in items]
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    for value, weight, ratio in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            capacity = 0

    return total_value

# Example
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(fractional_knapsack(items, capacity))
