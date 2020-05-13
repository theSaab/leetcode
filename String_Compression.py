'''
    this program condenses strings
    the string aabcccccaaa would become a2b1c5a3.
    if the new string is bigger, it just prints the original
'''

string = 'aaabbbaacccdee'
# string = 'abcdefghijkl'
compressedString = ''

position = 0
while position < len(string):
    count = 1
    x = 1
    while (position+x < len(string) and string[position] == string[position + x]):
        count += 1
        x += 1

    compressedString += string[position] + str(count)
    position += count

if (len(compressedString) < len(string)):
    print(compressedString)
else:
    print(string)
