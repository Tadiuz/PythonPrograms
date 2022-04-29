# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

import re

def solution(string,markers):
    
    
    new_str = string.split('\n')
    to_find = '|'.join(markers)
    compiled = re.compile('.*(?=('+ to_find + ')*)')
    print(compiled)
    
    final = [compiled.findall(i)[0].strip() if compiled.findall(i)  else i for i in new_str]
    return '\n'.join(final)
    



print(solution('apples, pears # and bananas\ngrapes\nbananas #!apples', ['#','!']))