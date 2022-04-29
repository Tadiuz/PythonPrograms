def dfs(node, graph):
    global counter
    global visited   
    neighbors = graph[node]
    for i in neighbors:
        if i not in visited:
            visited.add(i)
            counter+=1
            dfs(i, graph)

    return counter



def cycle():
    global graph
    maxim = 0
    for i in graph.keys():
        global counter
        counter = 0
        counter = dfs(i, graph)
        if counter !=None and counter > maxim:
            maxim=counter
    return maxim


graph = {}
def maxCircle(lista):
    global visited 
    
    global graph
    for i, j in lista:
        visited = set()
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]
        if j in graph:
            graph[j].append(i)
        else:
            graph[j] = [i]
        
        print(graph)
        maxim = cycle()
        print(maxim)

lista = [[1,2], [3,4], [2,3]]

maxCircle(lista)