



def happy(number):
    new_num = 0
    number = str(number)
    count = 0
    while new_num != 1:
        count += 1
        for char in number:
            char = int(char)**2
            new_num += char
    
        if new_num == 1:
            return True
            
        else:
            number = str(new_num)
            new_num = 0
        
        if count == 10000000:
            return False
        

happy(19)

