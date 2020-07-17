
# This program will sort a stack with numbers smallest to biggest
# very not fun

piece = [781, 2, 4, 5, 1, 124, 323221, 6, 435, 64, -12, 4, 7, 8, 99, 00, 56, 3, 16]
blank = []


def sort(stack):
    blank.append(stack[-1])
    stack.pop()

    while len(stack) >= 1:
        number = stack[-1]
        other = blank[-1]

        if (len(blank) != 0) and (number <= other):
            blank.append(number)
            stack.pop()

        elif number > other:
            stack.pop()
            while (len(blank) != 0) and (number > blank[-1]):
                stack.append(blank[-1])
                blank.pop()
            else:
                blank.append(number)

        else:
            stack.append(blank[-1])
            blank.pop()

    print(blank)


sort(piece)
