

def reverse(sentence):
    
    word = []
    output = ''

    for char in sentence:
        
        if char != ' ':
            word.append(char)
        
        else:
            for element in word[::-1]:
                output += element
            else:
                output += ' '
                word = []

    else:
        for element in word[::-1]:
            output += element

    return output

print(reverse("Let's take LeetCode contest"))
    
