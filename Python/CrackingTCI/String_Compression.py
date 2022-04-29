import unittest

def string_compression(string):
    counter = 0
    new_array = []
    for i in range(len(string)):
        if i != 0 and string[i] != string [i-1]:
            new_array.append(string[i-1] + str(counter))
            counter = 0
        counter +=1
    new_array.append(string[-1] + str(counter))
    return min(''.join(new_array), string, key=len)

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()