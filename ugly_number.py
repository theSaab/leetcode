

def ugly(number):
    count = 1
    ugly_num = 0
    while count <= number:
        ugly_num += 1

        if ugly_num == 1:
            count += 1

        elif (ugly_num / 7) % 1 == 0:
            continue

        elif (ugly_num / 5) % 1 == 0 or (ugly_num / 3) % 1 == 0 or (ugly_num / 2) % 1 == 0:
            print(count)
            print(str(ugly_num) + 'ugly')     
            count += 1

        else:
            continue
    else:
        return ugly_num

print(ugly(15))