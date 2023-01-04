# from typing import List


# def cheapest_flight(costs: List, a: str, b: str) -> int:
#     # your code here

#     direct = [cost[2] for cost in costs if a in cost and b in cost]
#     direct = direct[0] if direct else 0

#     indirects = []
#     indirect = []

#     for cost in costs:
#         if a in cost and b not in cost:
#             indirect.append(cost)
#             if cost[0] == a:
#                 temp = cost[1]
#             elif cost[1] == a:
#                 temp = cost[0]
#             for cost_b in costs:
#                 if temp in cost_b and b in cost_b and a not in cost_b:
#                     indirect.append(cost_b)
#             indirects.append(indirect)
#         indirect = []


#     ind_costs = []
#     for el in indirects:
#         if len(el) > 1:
#             ind_costs.append(el[0][2] + el[1][2])
#     indirect = min(ind_costs) if ind_costs else 0

#     if direct and direct:
#         return min(direct, indirect)
#     elif direct and not indirect:
#         return direct
#     else:
#         return indirect


from typing import List


def cheapest_flight(costs, a, b):

    route = [([cost], a) for cost in costs if a in cost]
    price = float('inf')

    while route:

        flight, last_postion = route.pop(0)
        start, mid, pr = flight[-1]
        current_postion = mid if start == last_postion else start

        if b in (start, mid):
            price = min(price, sum(price for _, _, price in flight))
        else:
            for next_step in [i for i in costs if current_postion in i and i not in flight]:
                route.append((flight + [next_step], current_postion))

    return price if price else 0 


print(cheapest_flight([["A","B",10],["A","C",20],["B","D",15],["C","D",5],["D","E",5],["E","F",10],["C","F",25]],"A","F"))
