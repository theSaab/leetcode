

def elimination(num):
    dik = {}
    count = 1
    for i in range(1, num+1):
        dik[count] = i
        count += 1

    print(dik)

    for i in range(1, len(dik) + 1, 2):
        dik[i] = ''
    
    for i in range(len(dik), 0, -2):
        print('herh')
        if dik[i] == '':
            print('reg')
            if i == 1:
                continue
            else:
                dik[i - 1] == ''

        else:
            print('here')
            dik[i] = ''
    
    # for i in     

    print(dik)

elimination(11)
