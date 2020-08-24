

def pairs(words):
    
    return_list = []
    count = 0
    index = -1
    for word in words:
        index += 1
        count += 1
        for element in words[count:]: 
            new_word = word + element 
            other_word = element + word

            if len(new_word) % 2 != 0:
                first_half = new_word[ : len(new_word)//2 ]
                second_half = new_word[ len(new_word)//2 + 1 : ]
                
                i = 1
                lst = []
                for char in first_half:
                   
                    if char != second_half[-(i)]:
                        break
                    else:
                        i += 1
                else:
                    lst.append(index)
                    lst.append(count)
            
                    return_list.append(lst)
            
            else:
                first_half = other_word[ : len(other_word)//2 ]
                second_half = other_word[ len(other_word)//2 + 1 : ]
                
                i = 1
                lst = []
                for char in first_half:
                   
                    if char != second_half[-(i)]:
                        break
                    else:
                        i += 1
                else:
                    lst.append(index)
                    lst.append(count)
            
                    return_list.append(lst)
    return return_list

print(pairs(["abcd","dcba","lls","s","sssll"]))