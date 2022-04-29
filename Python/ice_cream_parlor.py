from collections import defaultdict
from collections import deque 

def whatFlavors(cost, money):

    dt = defaultdict(deque)

    for i, n in enumerate(cost):
        dt[n].append(i + 1)
    
    new_arr = sorted(cost)

    i, j = 0, len(new_arr) - 1
    while i < j:

        if new_arr[i] + new_arr[j] > money:
            j -=1
        elif new_arr[i] + new_arr[j] < money:
            i +=1
        else:
            break
    
    
    print(dt)
    value1  = dt[new_arr[i]].popleft()
    value2  = dt[new_arr[j]].popleft()

    if value1 < value2:
        print(value1, value2)
    else:
        print(value2, value1)













print(whatFlavors([1, 4, 5, 3, 2], 4))