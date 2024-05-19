import itertools
import random

# 定義覆蓋設計參數
v = 49  # 總號碼數
k = 6   # 每次選擇的號碼數
t = 3   # 保證至少匹配的號碼數

# 生成所有可能的k組合
all_combinations = list(itertools.combinations(range(1, v + 1), k))

# 計算覆蓋設計
def covering_design(v, k, t):
    elements = list(range(1, v + 1))
    covering_sets = set()
    
    for subset in itertools.combinations(elements, t):
        found_combination = next(
            (comb for comb in all_combinations if set(subset).issubset(comb)),
            None
        )
        if found_combination:
            covering_sets.add(found_combination)
    
    return list(covering_sets)

# 生成覆蓋設計
covering_sets = covering_design(v, k, t)

# 隨機打亂覆蓋設計以確保隨機性
random.shuffle(covering_sets)

# 取前42個購買組合
final_tickets_42 = covering_sets[:42]

# 顯示前5個結果以供檢查
for i, ticket in enumerate(final_tickets_42[:5], 1):
    print(f"Ticket {i}: {sorted(ticket)}")

# 確認總購買組合數
len(final_tickets_42)
