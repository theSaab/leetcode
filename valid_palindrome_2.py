

def valid(s):
    
    if len(s) <= 4:
        if s[0] == s[-1]:
            return True 
        else:
            return False
    
    else:
        if len(s) % 2 != 0:
            middle = s[len(s)//2]
            first_half = s[:len(s)//2]
            second_half = s[len(s)//2+1:]
        else:
            first_half = s[:len(s)//2]
            second_half = s[len(s)//2:]

        count = 0
        reverse_first = '' 
        while count < 2:
            for char in first_half:
                reverse_first = char + reverse_first
                
            i = 0 

            for char in second_half:
                # print(count)
                # print('here')
                # print(char)
                # print(second_half[i])
                if reverse_first[i] != char:
                    count += 1
                else:
                    i += 1
            else:
                break

        if count == 2:
            return False
        else:
            return True


print(valid('eedede'))
