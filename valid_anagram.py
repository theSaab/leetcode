

s = "anagram"
t = "nagaram"

def anagram(s, t):
    
    dik = {}
    dik2 = {}

    for i,n in enumerate(s):
        if n in dik:
            dik[n] += 1
        else:
            dik[n] = 1
    
    for i,n in enumerate(t):
        if n in dik2:
            dik2[n] += 1
        else:
            dik2[n] = 1

    return (dik == dik2)

print(anagram(s, t))