
number = 400


def conversion(number, string=''):

    thousands = number//1000
    number = number//1000
    five_hundreds = number // 500
    number = number % 500
    hundreds = number//100
    fifty = number // 50
    tens = number//10
    fives = number//5

    string = thousands * 'M' + five_hundreds * 'D' + \
        hundreds * 'C' + fifty * 'L' + tens * 'X' + fives * 'V'
    print(string)


conversion(number)
