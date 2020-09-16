


# input S => str
# ({{[]}})
# edge cases
# not empty
# ([)] => not valid
# return type:
# True == valid
# False == not 
# from typing import Counter

# from pandas.core.reshape.reshape import stack

# {[{}}
# {[()]}]

# 1. create stack
# 2. add open-brackets to stack
# 3. once a close is found, pop the last item of stack
# 4. if they dont correspond, return false
# 5. else, continue
# 6. once iterated through string, return true

def test(s):
    if len(s) < 2:
        return False
            
    else:

        arr = []
        for element in s:
            print(element)
            if element == '{' or element == '[' or element == '(':
                arr.append(element)
            else:
                if element == '}':
                    print('here')
                    try:
                        if arr.pop() != '{':
                            return False
                    except:
                        return False
                elif element == ']':
                    print('hsdve')
                    try:
                        if arr.pop() != '[':
                            return False
                    except:
                        return False
                elif element == ')':
                    try:
                        if arr.pop() != '(':
                            return False
                    except:
                        return False

        else: 
            if len(arr) != 0:
                print(s)
                print('here')
                return False
            else:
                return True
                
print(test("(]"))

