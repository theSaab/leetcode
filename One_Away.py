

# this program check if 2 strings are more than one edit away
# the only edits allowed are : strings: insert a character,
# remove a character, or replace a character.

a = 'pale'
b = 'ale'

lena = len(a)
lenb = len(b)
count = 0


if abs(lena-lenb) > 1:
    print(False)
    
else:
    
    
