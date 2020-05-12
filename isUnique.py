
# this determines if all the characters in a words are unique 

word = 'excalibur'

for char in word:
    
    amount = word.count(char)
    
    # if there is more than one of same character 
    if amount > 1:
        print(False)
        break
    
else:
    # all are unique
    print(True)