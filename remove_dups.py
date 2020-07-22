
# this program removes the duplicates of a linked list
# not sure how to keep the same list though

from collections import deque

list = deque('aaaabfcdeefghilmnl')
blank = deque('')

for element in list:

    if element in blank:
        continue
    else:
        blank.append(element)

print(list)
print(blank)

