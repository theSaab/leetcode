

from collections import deque

#

piece = [ 781, 2, 4, 5, 1, 4, 6, 56, 3, 16]
min_stack = []

def push(number):
    stack.append(number)

    if min_stack[-1] > number:
        min_stack.append(number)

def pop():

    if min_stack[-1] == stack[-1]:
        min_stack.pop()
        stack.pop()
    
    else:
        stack.pop()

def min_pop():
    min_stack.pop()




def min(stack):

    min = None
    for i in range(len(stack)):

        if stack[0] <= stack[-1]:
            min = stack[0]
            stack.pop()

        else:
            stack.popleft()
    else:
        print(min)

min(piece)
