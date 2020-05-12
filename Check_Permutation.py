


# this program check if the string b contains all the letters
# of string a

a = 'excalibur'
b = 'burlex'

for char in b:

    # check if char is in a
    if (char in a) == False:
        print(False)
        break

# if for loop iterates through whole string b
else:
    print(True)
