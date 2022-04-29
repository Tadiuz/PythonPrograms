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

        if L[1] in Nodos:
            key1 = Nodos[L[1]]
            if key1 != key0:
                
                if len(pointer[key0]) > len(pointer[key1]):
                    var = key0
                    keys_1 = pointer[key1]
                    pointer[key1] = {}
                else:
                    var = key1
                    keys_1 = pointer[key0]
                    pointer[key0] = {}

                pointer[var].update(keys_1)
                for i in keys_1:
                    Nodos[i] = var
                key0  =var
 
        else:
            Nodos[L[1]] = key0
            pointer[key0].add(L[1])    
        aux = len(pointer[key0])


    elif L[1] in Nodos:
        var = Nodos[L[1]]
        keys = pointer[var]
        Nodos[L[0]] = var
        pointer[var].add(L[0])
        aux = len(pointer[var])
        
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
#Lista = [[6, 4], [5, 9], [8, 5], [4, 1], [1, 5], [7, 2], [4, 2], [7, 6]]
#Lista = [[1,2]]

#Lista = [[1,2],[3,4],[1,3],[5,7],[12,1]]

#Lista = [[1,2],[1,3]]

#Lista = [[int(v) for v in line.split()] for line in open('Input.txt')]
Lista = [[int(v) for v in line.split()] for line in open('Input2.txt')]


#Lista = [[78, 72], [67, 74], [65, 57], [65, 52], [70, 55], [74, 70], [58, 51], [70, 76], [69, 55], [64, 78], [67, 72], [69, 63], [77, 59], [69, 64], [70, 80], [66, 67], [71, 52], [60, 77], [80, 66], [70, 61]]

def shortest():
    maxim = 0
    longest = max(len(item) for item in pointer.values())
    return longest




def main():
    value = [calcula(i) for i in Lista]
    #print(value)
    # value = []
    # for i in Lista:
    #     s = calcula(i)
    #     value.append(s)
    #     print(s)


#main()

cProfile.run('main()')
