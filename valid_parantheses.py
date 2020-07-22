
'''
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''


def valid(string):

    if len(string) > 6:
        return False

    else:
        for char in string:
            if char == '{':
                str = ''
                if string.count(char) > 1:
                    print('Not valid')
                    break
                str += char
                for char in string[string.index(char)+1::2]:
                    if char == '}':
                        str += char
                    else:
                        continue
                if str != '{}':
                    return False
                    break

            elif char == '[':
                str = ''
                if string.count(char) > 1:
                    print('Not valid')
                    break
                str += char
                for char in string[string.index(char)+1::2]:
                    if char == ']':
                        str += char
                    else:
                        continue
                if str != '[]':
                    return False
                    break

            elif char == '(':
                str = ''
                if string.count(char) > 1:
                    print('Not valid')
                    break
                str += char
                for char in string[string.index(char)+1::2]:
                    if char == ')':
                        str += char
                    else:
                        continue
                if str != '()':
                    return False
                    break

        else:
            return True


print(valid('{][}'))
