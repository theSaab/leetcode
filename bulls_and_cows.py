

def guesser(secret, guess):
    bulls = 0
    cows = 0
    spare = secret

    for i,n in enumerate(guess):

        if n in secret and guess[i] == spare[i]:
            secret = secret[ : secret.index(n)] + secret[secret.index(n) + 1 : ]
            bulls += 1
            print('her')
            print(secret)
 
        elif n in secret:
            secret = secret[:secret.index(n)] + secret[secret.index(n) + 1:]
            cows += 1
            print('eseg')
            print(secret)
 
        else:
            continue

    hint = str(bulls) + 'A' + str(cows) + 'B'

    return hint

print(guesser('1122', '1222'))
    
