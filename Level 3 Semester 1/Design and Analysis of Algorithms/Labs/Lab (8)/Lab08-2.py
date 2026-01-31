def job_sequencing(jobs):
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
