

string = 'abcabcabcabacbabccsdawrt'
arr = []


def long_sub(word):
    stri = ''
    arr = []
    for char in word:
        if char not in stri:
            stri += char
        else:
            arr.append(stri)
            stri = ''
    else:
        arr.append(stri)
        length = 0
        for element in arr:
            if len(element) > length:
                length = len(element)
            else:
                continue
        else:
            print(length)


long_sub(string)
