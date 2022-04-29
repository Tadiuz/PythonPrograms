import unittest


def rotate_matrix(matrix):
    for i in range(len(matrix)//2):
        for j in range(i, len(matrix)-1-i):
            top = matrix[i][j]
            right = matrix[j][-1-i]
            bottom = matrix[-1-i][-1-j]
            left = matrix[-1-j][i]

            matrix[i][j] = left
            matrix[j][-1-i] = top
            matrix[-1-i][-1-j] = right
            matrix[-1-j][i]  = bottom

    
    print(matrix)
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()