

# Given two strings, original and rotated, write code to check if rotated is
# a rotation of original using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(original, rotated):
    # find the first letter of the rotated word
    first = rotated[0]
    # find where to start in the original word
    begin = -original.find(first)
    
    # iterate through original word
    for char in original:
        # determine if characters are following with each other
        if char == rotated[begin]:
            begin += 1
            continue
        # not following = not rotation
        else:
            print(False)
            break
    # if successfully iterated through whole word, it is a rotation
    else:
        print(True)
        
isSubstring('waterbottle', 'terbottlewa')
    
    
    