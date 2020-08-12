

def row(list):

    bank = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for element in list:

        count = 0
        i = 0
        position = 0
        while i < len(element):
            print(element[position])
            if element[position] in bank[count]:
                i += 1
                position += 1
                print('hhere')
                continue
            else:
                i = 0
                print('heacsac')
                count += 1
        else:
            return element

print(row(["Hello", "Alaska", "Dad", "Peace"]))
