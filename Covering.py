import itertools
import random
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

# 生成購買的號碼組合，確保每個組合有6個號碼
def generate_tickets(total_combinations, select_numbers=6):
    tickets = []
    used_numbers = set()

    # 隨機打亂總組合以確保隨機性
    random.shuffle(total_combinations)

    for combination in total_combinations:
        current_ticket = set(combination)
        if len(current_ticket) == select_numbers:
            tickets.append(sorted(current_ticket))
        else:
            while len(current_ticket) < select_numbers:
                additional_combination = next(
                    (c for c in total_combinations if not current_ticket.intersection(c)),
                    None
                )
                if additional_combination:
                    current_ticket.update(additional_combination)
                else:
                    break
            tickets.append(sorted(current_ticket))

    # 確保每個購買組合只有6個號碼
    final_tickets = []
    for ticket in tickets:
        if len(ticket) > select_numbers:
            final_tickets.append(sorted(ticket[:select_numbers]))
        else:
            final_tickets.append(ticket)

    return final_tickets

# 至少中3個號碼的組合
total_combinations_3 = calculate_total_combinations(groups, 3)
tickets_3 = generate_tickets(total_combinations_3)

# 隨機打亂購買的號碼組合以確保隨機性
random.shuffle(tickets_3)

# 取前42個購買組合
final_tickets_42 = tickets_3[:42]

# 顯示前5個結果以供檢查
for i, ticket in enumerate(final_tickets_42[:5], 1):
    print(f"Ticket {i}: {ticket}")

# 確認總購買組合數
len(final_tickets_42)
