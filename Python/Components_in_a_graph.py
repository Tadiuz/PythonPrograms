from collections import defaultdict
from collections import deque 


global max
max = []

global min
global visited

visited = set()

def solve(s, dt):
    global max
    global visited

    visited.add(s)
    counter = 1
    queue = deque()
    
    queue.append(s)

    while queue:
        value = queue.popleft()
        ngb = dt[value]

        for i in ngb:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                counter  += 1
    max.append(counter)



def componentsInGraph(gb):
    # Write your code here
    dt = defaultdict(list)

    for i in gb:
        dt[i[0]].append(i[1])
        dt[i[1]].append(i[0])


    for i in dt:
        if i not in visited:
            solve(i, dt)




componentsInGraph([[1, 6], [2, 7], [3, 8], [4, 9], [2, 6]])

print(max)