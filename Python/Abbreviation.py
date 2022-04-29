

def first_traversal(a,b,matrix):
    for i in range(len(a)):
        if i == 0:
            matrix[0][i] = True

        elif a[i].islower() and matrix[0][i-1] == True:
            matrix[0][i] = True

    return matrix


def abbreviation(a, b):

    a = " " + a
    b = " " + b

    matrix = [[False for i in range(len(a))] for i in range(len(b))]

    matrix = first_traversal(a, b, matrix)


    for i in range(1, len(b)):
        for j in range(1, len(a)):

            if a[j].islower():
                if a[j].lower() == b[i].lower() and (matrix[i][j-1] == True or matrix[i-1][j-1] == True):
                    matrix[i][j] = True
                elif a[j].lower() != b[i].lower():
                    matrix[i][j] = matrix[i][j-1]
            else:
                if a[j] == b[i] and matrix[i-1][j-1] == True:
                    matrix[i][j] = True
                else:
                    matrix[i][j] = False

    return matrix[-1][-1]


print(abbreviation("dDaBbcd", "DBcd"))