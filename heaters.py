

def license(s, k):
    final = ''
    count = 0 
    piece = ''
    for char in s:
        while count < k:    
            if char == '-':
                break
            else:
                print(count)
                print(char)
                count += 1
                char = char.upper()
                piece += str(char)
                break
        else:
            print('herhe')
            count = 0
            final += str(piece) + '-'
            print(final)    
    else:
        print(final)

license("5f3Z-2e-9-w", 4)
    