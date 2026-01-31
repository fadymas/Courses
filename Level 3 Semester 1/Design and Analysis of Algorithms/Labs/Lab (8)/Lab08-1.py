def classroom_schedule(classes): # O(n log n)
    classes.sort(key=lambda x: x[1])

    selected = []
    last_end = 0

    for start, end in classes:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

# Example
classes = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
print(classroom_schedule(classes))

def job_sequencing(jobs): # O(n^2)
    jobs.sort(key=lambda x: x[1], reverse=True)

    max_deadline = max(j[2] for j in jobs)
    schedule = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, profit, deadline in jobs:
        for slot in range(deadline, 0, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                total_profit += profit
                break

    return schedule, total_profit

# Example
jobs = [('A', 100, 2), ('B', 19, 1), ('C', 27, 2), ('D', 25, 1), ('E', 15, 3)]
print(job_sequencing(jobs))

def fractional_knapsack(items, capacity): #O(n log n)
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
