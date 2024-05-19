import itertools
import math

# 定義組
groups = [list(range(1 + i * 7, 8 + i * 7)) for i in range(7)]

# 計算每組中的組合
def calculate_group_combinations(group, k):
    return list(itertools.combinations(group, k))

# 計算總組合
def calculate_total_combinations(groups, k):
    total_combinations = []
    for group in groups:
        total_combinations.extend(calculate_group_combinations(group, k))
    return total_combinations

# 生成購買的號碼組合
def generate_tickets(total_combinations, select_numbers=6):
    tickets = []
    for i in range(0, len(total_combinations), select_numbers):
        ticket = set()
        for combination in total_combinations[i:i + select_numbers]:
            ticket.update(combination)
        tickets.append(sorted(ticket))
    return tickets

# 至少中2個號碼的組合
total_combinations_2 = calculate_total_combinations(groups, 2)
tickets_2 = generate_tickets(total_combinations_2)

# 至少中3個號碼的組合
total_combinations_3 = calculate_total_combinations(groups, 3)
tickets_3 = generate_tickets(total_combinations_3)

tickets_2[:5], tickets_3[:5]  # 顯示前5個結果以供檢查

print tickets_3
