

def single_num(list):

    dik = {}
    arr = list
    for i, n in enumerate(list):
        if n in dik:
            dik[n] += 1
        else:
            dik[n] = 1
    else:
        final = []
        for n in dik:
            if dik[n] == 1:
                final.append(n)

        return final


print(single_num([1, 2, 1, 3, 2, 5]))
