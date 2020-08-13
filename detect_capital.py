

def detect(word):

    count = 0
    first = False
    if word[0] == word[0].upper():
        first = True
    for char in word[1:]:
        if char.upper() == char:
            count += 1
        else:
            continue
    else:
        if first == True and count == len(word) - 1:
            print('he')
            return True
        elif first == True and count > 1:
            print('hsdv')
            return False
        elif count == 0:
            return True


print(detect('g'))