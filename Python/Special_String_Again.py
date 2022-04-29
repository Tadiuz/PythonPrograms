


def first_pass(string):
    lista = [{string[0]:1}]
    counter = 0
    value = lista[counter]
    for i in range(1,len(string)):
        v = string[i]
        if v in value:
            value[v] +=1
        else:
            counter +=1
            lista.append({})
            value = lista[counter]
            value[v] = 1
    return lista

def first_calc(value):
    return (value*(value-1)) // 2



def second_calc(string, values):
    counter = 0
    for i in range(len(string)-1):
        val = string[i:i+3]
        if val == val[::-1] and values[i+1] == 1:
            s = min(values[i], values[i+2])
            counter += (1*s)
    
    return counter

def main(n, s):
    counter = n
    lista = first_pass(string)
    print(lista)

    keys = ""
    values = []
    for i in lista:
        for j, k in i.items():
            keys += j
            values.append(k)
            if k >1:
                counter += first_calc(k)

    print(f"first counter {counter}")
    counter += second_calc(keys, values)

    print(f"second_calc counter {counter}")

    return counter
       
#string = "aaabaaa"  #[{"a":3, "s":1, "a":3, "s":1, "d":3}]
string = "aaabaaaba"  #[{"a":3, "s":1, "a":3, "s":1, "d":3}]


value = main(len(string), string)

print(f"Values is {value}")

