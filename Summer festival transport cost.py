n = int(input())
p = int(input())
q = int(input())
min_cost=99999999
for bus in range(n // 80 + 1):
    remaining = n - bus * 80
    shuttle=remaining//8
    if remaining%8!=0:
        shuttle+=1
    
    cost = (bus * p + shuttle * q) * 75

    if bus == 0:
        min_cost = cost
    elif cost < min_cost:
        min_cost = cost

print(min_cost)
