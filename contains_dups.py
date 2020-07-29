

list = [2, 14, 18, 22, 22]


def dups(list):
    
    dick = {}
        
    for i,n in enumerate(nums):
        if n in dick:
            return True
        else:
            dick[n] = i
    else: 
        return False
    
print(dups(list))
