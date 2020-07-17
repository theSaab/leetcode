

from collections import deque

piece = deque([781, 2, 4, 5, 1, 4, 6, 56, 3, 16])


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
