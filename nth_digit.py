


def digit(digit):


    dik = {}
    count = 0
    for i in range(digit+1):
        for i,n in enumerate(str(i)):
            # print(str(n) + ' n')
            # print(str(i) + ' i')
            dik={}
            dik[count ] = n
            # print(str(count) + ' count')
            count += 1

    return dik[digit]

print(digit(10000000))