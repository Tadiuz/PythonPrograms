# At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

# The restriction is that the characters in part1 and part2 should be in the same order as in s.

# The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

# For example:

# 'codewars' is a merge from 'cdw' and 'oears':

#     s:  c o d e w a r s   = codewars
# part1:  c   d   w         = cdw
# part2:    o   e   a r s   = oears



def is_merge(s, part1, part2):

    if len(s) != len(part1 + part2):
        return False
    if len(s) == 0:
        return True
    if part1 and s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    elif part2 and s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False

    