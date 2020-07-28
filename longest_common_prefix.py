

choices = ["flower","flow","owight"]

def longest_pre(words):
    
    pos = 0
    streak = 0 
    char = None
    iter = 100 
    # for word in words:
    x = 0

    # for i in range(iter):
    while x < iter:
        for word in words:
            if len(word) < iter:
                iter = len(word)

            elif char == None:
                char = word[pos]

            elif word[pos] == char:
                continue
                
            else:
                break
        else:
            x += 1
            char = None
            pos += 1
            streak += 1

    print(words[0][:streak])

longest_pre(choices)