possible = False
dt = {}
def recursive_abb(a, b):
    print(a,b)
    global possible

    if (not a and not b):
        return True
    elif len(b) > len(a):
        return False

    if not b and not(any(map(lambda x: x.isupper(), a))):
        return True
    elif not b and (any(map(lambda x: x.isupper(), a))):
        return False

             


    if possible == False:
        if a + "#" + b in dt:
            return dt[a + "#" + b]
        if a[-1].islower():
            a1 = a[:-1]
            a2 = a[:-1] + a[-1].upper()
            recursive_abb(a1, b)
            recursive_abb(a2, b)
        
        else:
            if a[-1] == b[-1].upper():
                a = a[:-1]
                b = b[:-1]
                possible = recursive_abb(a,b)
            else:
                
                return False

    dt[a+"#"+b] = possible
    return possible


def abbreviation(a, b):

    if recursive_abb(a, b):
        return ("YES")
    else:
        return ("NO")

print(abbreviation("daBcd", "ABC"))