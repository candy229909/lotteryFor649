import math

# Define the group sizes
group_sizes = [16, 16, 17]

# Calculate combinations within each group
def calculate_combinations(group_size, k):
    return math.comb(group_size, k)

# Calculate minimum tickets needed using the pigeonhole principle
def min_tickets(group_sizes, k):
    total_tickets = 0
    for size in group_sizes:
        total_tickets += calculate_combinations(size, k)
    return total_tickets

# Calculate for at least 2 matches in any group
min_tickets_2 = min_tickets(group_sizes, 2)

# Calculate for at least 3 matches in any group
min_tickets_3 = min_tickets(group_sizes, 3)

min_tickets_2, min_tickets_3


