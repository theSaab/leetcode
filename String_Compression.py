

# this program condenses strings
# the string aabcccccaaa would become a2b1c5a3.
# if the new string is bigger, it just prints the original

string = 'aaabbbcccdee'
position = 0
x = 1

while position < len(string):
    count = 1
    x = 1
    
    while (string[position] == string[position + x]):
        count += 1
        x += 1
    
    print(string[position] + str(count), end='')
    
    print('\nposition ' + str(position))
    print('count ' + str(count))    
    position += count
    


print('\n')