
'''
mplement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
# How is this a leetcode???????

def str(haystack, needle):
    if needle in haystack:
        print(haystack.index(needle))
    else:
        print(-1)

str('aaaaaaaaa', 'bb')