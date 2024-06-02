import heapq

def min_cost_to_connect_cables(cables_list):
    heapq.heapify(cables_list)

    total_cost = 0

    while len(cables_list) > 1:
        cable1 = heapq.heappop(cables_list)
        cable2 = heapq.heappop(cables_list)

        cost = cable1 + cable2
        total_cost += cost

        heapq.heappush(cables_list, cost)

    return total_cost

cables_list = [8, 4, 6, 12]
print(min_cost_to_connect_cables(cables_list))  # 58
