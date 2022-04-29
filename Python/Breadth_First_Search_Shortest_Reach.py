from collections import deque


# def reconstruct(s, e, path):
#     exist = []
#     value = e
#     while value != 'NA':
#         exist.append(value)
#         if value == s:
#             break
#         value = path[value]

#     if exist[-1] == s:
#         return exist
#     else:
#         return -1

def reconstruct(s, e, path):
    exist = []
    value = e
    while value != 'NA':
        exist.append(value)
        if value == s:
            break
        value = path[value]

    if exist[-1] == s:
        return (len(exist)-1)*6
    else:
        return -1


def search(s, dt):
    visited = set()
    path = ['NA' for i in range(len(dt))]
    queue = deque([s])

    while queue:
        node_val = queue.popleft() 
        visited.add(node_val)
        neigh = dt[node_val]

        for i in neigh:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                path[i] = node_val
    return path


def get_adj(dt, edges):

    for i in range(len(edges)):
        val = edges[i]
        dt[val[0]].append(val[1])
        dt[val[1]].append(val[0])

    return dt

def bfs(n, m, edges, s):
    dt = {}
    for i in range(n+1):
        dt[i] = []
    dt = get_adj(dt, edges)

    path = search(s, dt)
    print(dt)
    print(path)
    inte = []
    for i in range(len(dt)):
        if i !=s and i!=0:
            inte.append(reconstruct(s, i, path))

    print(inte)


    # Write your code here
    
    



#bfs(5,2,[[1, 2], [1, 3], [3,4]],1)
bfs(3,2,[[2, 3]],2)
#bfs(11,2,[[1, 2], [1, 3], [2, 4], [4, 5], [4, 6], [6, 7], [3, 7], [8,9], [5,10], [10,11], [6,11]],1)