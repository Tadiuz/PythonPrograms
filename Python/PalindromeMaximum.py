


def highestValuePalindrome(s, n, k):
    counter = 0
    ss1 = list(map(int, list(s)))
    ss2 = list(map(int, list(s[::-1])))
    new_val = [(i - j) for i, j in zip(ss1, ss2)]
    movements = k
    index = []
    for i in range(len(new_val)//2):
        if new_val[i]!=0 and counter <= movements:

            if ss1[i] > ss1[-i-1]:
                ss1[-i-1] = ss1[i]
                index.append(-i-1)
            else:
                ss1[i] = ss1[-i-1]
                index.append(i)
            counter +=1
            
        elif counter > movements:
            return -1
    return ss1, index, counter


k = 3

def find_second_value(ss1,index, counter, k):
    dt = {}
    available = k - counter

    ss2 = ss1.copy()
    for i in index:
        if i < 0:
            dt[abs(i+1)] = dt.get(abs(i+1), 0) + 1
        else:
            dt[i] = dt.get(i, 0) + 1

    if available == 1 and len(ss1)%2 !=0:

        ss2[len(ss1)//2] = 9
        return ss2

    keys = sorted(list(dt.keys()))
    for i in keys:

        if available <=1:
            break

        ss2[i] = 9
        ss2[-i-1] = 9
        available -=2
    
    if available == 1 and len(ss1)%2 !=0:

        ss2[len(ss1)//2] = 9
    return ss2

original = "092282"

ss1, index, counter = highestValuePalindrome("092282", 0, k)


print(original)
print(ss1, index, counter)

print(find_second_value(ss1,index, counter, k))
