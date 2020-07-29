

def power(num):

    while num != 1 and num != 0:
        num = num / 3

    if num == 0:
        return False
    else:
        return True


print(power(27))
