import unittest

def pal_perm(s_array):
    dt = {}
    countodd = 0
    for i in s_array.lower():
        if i.isalnum():
            dt[i] = dt.get(i , 0) + 1
            if dt[i] %2 != 0:
                countodd +=1
            else:
                countodd -=1
    return countodd <=1
            


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()