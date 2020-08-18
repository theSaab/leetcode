

def self_dividing(left, right):

    arr =[]

    for i in range(left, right+1):

        if str(0) not in str(i):
            for char in str(i):
                if int(i) % int(char) != 0:
                    break
            else:
                arr.append(i)

    return arr

print(self_dividing(1,22))