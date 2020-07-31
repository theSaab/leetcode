


def find(list):

    dik = {}
    for i,n in enumerate(list):
        if n in dik:
            return n
            break
        else:
            dik[n] = i

print(find([3,1,3,4,2]))