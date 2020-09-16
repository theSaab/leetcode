


def remove(S):

    arr = []
    for char in S:
        arr.append(char)
    
    for i in range(len(arr)):
        for index,element in enumerate(arr):
            try:
                if element == arr[index + 1]:
                    arr.pop(index + 1)
                    arr.pop(index)
            except:
                continue
    S = ''

    for element in arr:
        S += element
    return S

print(remove('aababaab'))