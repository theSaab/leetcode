


def row(list):
    output = []
    bank = ['zxcvbnmZXCVBNM','ASDFGHJKLasdfghjkl','QWERTYUIOPqwertyuiop']
    for element in list:
        count = 0
        i = 0
        while i < len(element) and count < 3:
            if element[i] not in bank[count]:
                print(count)
                count += 1
                i = 0
            else:
                i += 1
                continue
        else:
            print(str(i) + ' i')
            print(len(element))
            if i == len(element):
                output.append(element)

    return output

print(row( ["Hello", "Alaska", "Dad", "Peace"]))
