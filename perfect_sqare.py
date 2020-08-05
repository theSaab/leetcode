


def perfect(num):

    for i in range(num//2 + 2):

        if i**2 == num:
            return True

    else:
        return False

print(perfect(1))