import unittest

def zero_matrix(matrix):
    rows = set()
    columns = set()

    for i, n in enumerate(matrix):
        for j, k in enumerate(n):
            if k == 0:
                rows.add(i)
                columns.add(j)

    for i in columns:
        zero_column(i, matrix)
    for i in rows:
        zero_row(i, matrix)
    return  matrix

def zero_row(row, matrix):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def zero_column(column, matrix):
    for i in range(len(matrix)):
        matrix[i][column] = 0


matrix = [ 
    [3,4,5,7],
    [6,9,2,1],
    [3,4,0,2],
    [9,2,1,3],
    [0,5,8,7]]



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()