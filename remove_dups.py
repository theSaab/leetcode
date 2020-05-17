
# this program removes the duplicates of a linked list
# not sure how to keep the same lsit though

from collections import deque

list = deque('abfcdeefghilmnl')
blank = deque('')

for element in list:

    if element in blank:
        continue
    else:
        blank.append(element)

print(list)
print(blank)
