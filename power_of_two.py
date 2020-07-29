
number = 14

def power(num):

    while num != 1 and num != 0:
        num = num / 2

    if num == 0:
        return False
    else:
        return True

print(power(number))