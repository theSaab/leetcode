

def counter(J, S):
    
    final = 0
    for char in J:
        final += S.count(char)

    return final

    