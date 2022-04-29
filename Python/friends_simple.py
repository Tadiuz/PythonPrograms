



lista = [[1000000000,23],[11,3778],[7,47], [11, 1000000000]]




l2 = []

for i in lista:
    l2.append(set(i))


maxim = 0

new = []
l1 = []
for k in l2:
    l1.append(k)
    for i in range(len(l1)):
        value = l1[i]
        for j in range(i,len(l1)):
            if len(value & l1[j]) >0:
                value = value.union(l1[j])
        count=len(value)
        if count > maxim:
            maxim = count
    print(maxim)


