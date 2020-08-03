

def move(list):

    for i,n in enumerate(list):
        if n == 0:
            list.insert(len(list),n)
            list.remove(n)
    return list

print(move([0,1,0,3,12,9]))