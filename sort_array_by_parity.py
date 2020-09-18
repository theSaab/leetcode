


from os import listxattr


def sort(A):

    arr = []

    for element in A:
        if element % 2 != 0:
            arr.append(element)
        else:
            arr.insert(0, element)

    return arr