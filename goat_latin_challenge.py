

def goat(S):

    vowels = 'aeiouAEIOU'
    word = ''
    arr = []

    for char in S:
        if char != ' ':
            word += char
        else:
            arr.append(word)
            word = ''
    else:
        arr.append(word)

    index = 0
    return_arr = []
    for element in arr:
        index += 1
        if element[0] in vowels:
            element += 'ma'
        else:
            element = element[1:] + element[0] + 'ma'

        element += 'a' * index

        return_arr.append(element)
    
    coded = ''
    for element in return_arr:
        coded += element + ' '

    return coded


print(goat("I speak Goat Latin"))