

def complete(licensePlate, words):
    
    len = 100
    num = '1234567890'
    index = 0
    i = 0

    while i < len(licensePlate):
        if licensePlate[i] not in num:
            if licensePlate[i] in words[index]:
                i += 1
            else:            
                index += 1
                break
        
    else:
        return words[index]

print(complete("1s3 PSt", ["step", "steps", "stripe", "stepple"]))