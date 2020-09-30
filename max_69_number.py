



def change(num):
    for i,char in enumerate(str(num)):
        if char == '6':
            num = str(num)[:i] + '9' + str(num)[i+1:]
            return num
    return num