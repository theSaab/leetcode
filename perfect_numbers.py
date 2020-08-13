



def perfect(num):
    count = 0
    for i in range(1, num//2+1):
        if (num / i) % 1 == 0 :
            count += i
    else:
        
        if count == num:
            return True
        else:
            return False

print(perfect(28))