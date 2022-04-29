import re


from re import finditer


for match in finditer("![a-z]", "!f!g!f!g!f"):
    print(match.span(), match.group())


