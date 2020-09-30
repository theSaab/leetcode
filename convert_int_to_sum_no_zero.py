

def convert(n):

    arr = []

    for i in range(1, n):
        if '0' not in str(n-i) and '0' not in str(i):
            print(n-i)
            arr = [i, n-i]
            return arr
    
print(convert(11))