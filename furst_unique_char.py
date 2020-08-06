


def unique(word):

    dik = {}
    for i,char in enumerate(word):
        if char in dik:
            dik[char] += 1
        else:
            dik[char] = 1
    
    else:
        for node in dik:
            if dik[node] == 1:
                print(word.index(node))
                break
        else:
            return -1

unique('leetcode')
