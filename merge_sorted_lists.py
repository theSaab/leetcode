

first = [1, 1, 1]
second = [1, 1, 5]


def merge(list1, list2):
    new = []
    pos = 0
    num = 0

    if len(list1) > len(list2):
        num = len(list2)
        long = list1
    else:
        num = len(list1)
        long = list2

    for i in range(num):
        if list1[pos] < list2[pos]:
            new.append(list1[pos])
            new.append(list2[pos])
        else:
            new.append(list2[pos])
            new.append(list1[pos])
        pos += 1
    else:
        for element in long[pos:]:
            new.append(element)

    print(new)


merge(first, second)
