

def digits(number):
    new = 0
    while len(str(number)) > 1:
        for char in str(number):
            char = int(char)
            new += char

        number = new
        new = 0
        
    return number

digits(38)
