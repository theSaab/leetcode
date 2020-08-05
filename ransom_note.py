


def ransom( note, magazine):
    
    mag_arr = []

    for n in (magazine):
        mag_arr.append(n)
    for char in note:
        try:
            mag_arr.remove(char)
        
        except:
            return False
    else:
        return True
    
print(ransom('aa', 'aab'))

    
