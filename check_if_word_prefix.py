


def check( sentence, searchWord ):

    word = ''
    # arr = []
    count = -1
    for char in sentence:
        if char != ' ':
            word = word + char
        else:
            count += 1
            if searchWord in word:
                if searchWord(0) == word(0):
                    return True

            # arr.append[word]
            # word = ''
    else:
        return -1
    


        
    