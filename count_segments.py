

def count_segments(string):
    if len(string) == 0:
        return 0
    else:

        arr = []
        word = ''
        for char in string:
            if char != ' ':
                word += char
            else:
                if word != '':
                    arr.append(word)
                    word = ''

        else:
            if word != '':
                arr.append(word)
        return len(arr)


print(count_segments("                "))
