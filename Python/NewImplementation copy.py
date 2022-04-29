from collections import defaultdict
import cProfile
import itertools

counter_p = 0
Nodos = {}
pointer = defaultdict(set)
maxim = 0




def calcula(L):
    global Nodos
    global maxim
    global counter_p
    global pointer
    aux = 0

    if L[0] in Nodos:
        key0 = Nodos[L[0]]
        keys_0 = pointer[key0]

        if L[1] in Nodos:
            key1 = Nodos[L[1]]
            keys_1 = pointer[key1]
            pointer[counter_p].update(keys_1)

            #Nodos.update(dict(zip(keys_1, itertools.repeat(counter_p))))
            for i in keys_1:
                Nodos[i] = counter_p
            pointer[key1] = {}
        else:
            pointer[counter_p].add(L[1])

        pointer[counter_p].update(keys_0)


        #Nodos.update(dict(zip(keys_0, itertools.repeat(counter_p))))
        for i in keys_0:
            Nodos[i] = counter_p

        pointer[key0] = {}
        aux = len(pointer[counter_p])
        
        Nodos[L[0]] = counter_p
        Nodos[L[1]] = counter_p


    elif L[1] in Nodos:
        var = Nodos[L[1]]
        keys = pointer[var]
        pointer[counter_p].update(keys)

        #Nodos.update(dict(zip(keys, itertools.repeat(counter_p))))
        for i in keys:
            #pointer[counter_p].add(i)
            Nodos[i]=counter_p

            
        pointer[var] = {}
        Nodos[L[0]] = counter_p
        pointer[counter_p].add(L[0])
        aux = len(pointer[counter_p])
        
    else:
        Nodos[L[0]] = counter_p
        Nodos[L[1]] = counter_p
        pointer[counter_p].update(L)
        aux = len(pointer[counter_p])
    counter_p +=1

    if aux > maxim:
        maxim = aux
    return maxim

#Lista = [[1,2],[3,4],[5,1],[4,5],[7,1],[3,9],[8,10],[10,4],[100,1000],[34,100],[43,34],[1,34]]

#Lista = [[1000000000,23],[11,3778],[7,47],[11,1000000000]]
#Lista = [[1,2],[3,4],[1,3],[5,7],[5,6],[7,4]]
#ista = [[6, 4], [5, 9], [8, 5], [4, 1], [1, 5], [7, 2], [4, 2], [7, 6]]
#Lista = [[1,2]]

#Lista = [[1,2],[3,4],[1,3]]

#Lista = [[1,2],[1,3]]

Lista = [[int(v) for v in line.split()] for line in open('Input.txt')]

def shortest():
    maxim = 0
    longest = max(len(item) for item in pointer.values())
    return longest




def main():
    value = [calcula(i) for i in Lista]

    #print(value)


#main()

cProfile.run('main()')
