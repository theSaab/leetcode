


# # input S => str
# # ({{[]}})
# # edge cases
# # not empty
# # ([)] => not valid
# # return type:
# # True == valid
# # False == not 
# # from typing import Counter

# # from pandas.core.reshape.reshape import stack

# # {[{}}
# # {[()]}]

# # 1. create stack
# # 2. add open-brackets to stack
# # 3. once a close is found, pop the last item of stack
# # 4. if they dont correspond, return false
# # 5. else, continue
# # 6. once iterated through string, return true

# # def test(s):
# #     if len(s) < 2:
# #         return False
            
# #     else:

# #         arr = []
# #         for element in s:
# #             print(element)
# #             if element == '{' or element == '[' or element == '(':
# #                 arr.append(element)
# #             else:
# #                 if element == '}':
# #                     print('here')
# #                     try:
# #                         if arr.pop() != '{':
# #                             return False
# #                     except:
# #                         return False
# #                 elif element == ']':
# #                     print('hsdve')
# #                     try:
# #                         if arr.pop() != '[':
# #                             return False
# #                     except:
# #                         return False
# #                 elif element == ')':
# #                     try:
# #                         if arr.pop() != '(':
# #                             return False
# #                     except:
# #                         return False

# #         else: 
# #             if len(arr) != 0:
# #                 print(s)
# #                 print('here')
# #                 return False
# #             else:
# #                 return True
                
# # # print(test("(]"))


# # stack without using stack

# # stack = []

# # from collections import deque 
# # queue = deque(["Ram", "Tarun", "Asif", "John"]) 

# # stack.append()

# # from io import StringIO


# # string S
# # return longest palindromic substring in S
# # non empty
# # no nums
# # including capitals
# # upper are same as lower
# # 100 characters

# # 0. iterate through string.
# # 1. for char in S:
# # 2. check if left == right: 
# # 3. add 1, check if same, add count
# # 6. else, check right char
# # 7. repeat 3
# # 7.5, find index
# # 8. return string

# def palindrome(S):

#     for i in range(len(S)):
        
#         char_index = 0
#         count = 0
#         pointer = 0

#         if S[i-1] == S[i+1]:
#             pointer += 1
#             try:
#                 for element in S[i+2:]:
#                     if element == S[i-2-pointer]:
#                         pointer += 1
#                         continue
#                     else:
#                         if pointer * 2 + 1 > count:
#                             count = pointer * 2 + 1
#                             char_index = i
#                             pointer = 0
#             except:
#                 if pointer * 2 + 1 > count:
#                     count = pointer * 2 + 1
#                     char_index = i
#                     pointer = 0


#         elif S[i+1] == S[i]:
#             pointer += 1
#             try:
#                 for element in S[i+2:]:
#                     if element == S[i-1-pointer]:
#                         pointer += 1
#                         continue
#                     else:
#                         if pointer * 2 > count:
#                             count = pointer * 2
#                             char_index = i
#                             pointer = 0
#             except:
#                 if pointer * 2 > count:
#                     count = pointer * 2
#                     char_index = i
#                     pointer = 0                    

#     substring = S[char_index - count//2:char_index + count//2 ]

#     return substring

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s_list = list(s)
#         if not s:
#             return ''
#         longest_sub = s[0]
#         temp_sub = ''
#         for count in range(len(s)-1):
#             if s[count] == s[count+1]:
#                 high = count+1
#                 low = count
#                 while high < len(s) and low >= 0 and s[low] == s[high]:
#                     temp_sub = s[low:high+1]
#                     high += 1
#                     low -= 1
#                 if len(temp_sub) > len(longest_sub):
#                     longest_sub = temp_sub
                    
#         for index in range(1, len(s)-1):
#                 high = index+1
#                 low = index-1
#                 while high < len(s) and low >= 0 and s[low] == s[high]:
#                     temp_sub = s[low:high+1]
#                     high += 1
#                     low -= 1
#                 if len(temp_sub) > len(longest_sub):
#                     longest_sub = temp_sub
            
#         # return longest_sub
#         for index in range(1, len(s)-1):
#                 high = index+1
#                 low = index-1
#                 while high < len(s) and low >= 0 and s[low] == s[high]:
#                     temp_sub = s[low:high+1]
#                     high += 1
#                     low -= 1
#                 if len(temp_sub) > len(longest_sub):
#                     longest_sub = temp_sub
#         return longest_sub


# print(Solution('abbaabbaabbaa'))

'''

determine whether int is palidrome
return boolean
non empty
non negative [0, 100000]
whole ints
only ints in int

1234321
12321

0. og_num = num
1. new_num = 0
2. while num > 0 :
3. new_num = new_num * 10 + num%10
4. num = num//10
5. return new_num == og_num

'''

# def palidrome_verification( num ):

#     og_num = num
#     new_num = 0

#     while num > 0:
#         new_num = new_num * 10 + num % 10
#         num = num // 10
    
#     return new_num == og_num

# palidrome_verification()


'''
input: singly linked list
query: find out if its a palindrome
output: return boolean
edge cases:
    can be empty   
    proper list
    non infinite 
only ints                                  

1 2 3 4 3 2 1

1 2 2 1
arr = []

1. arr = []
2. find middle 
3. 2 pointers 
4. pointer1 self.head
5. pointer2 self.head.next
6. while pointer2.next != None 
6.5. arr.append(pointer1.data)
7. pointer1 = pointer1.next
8. pointer2 = pointer2.next
9. pointer2 = pointer2.next
10. if len(llist) % 2 != 0:
        arr.pop()
11. while len(arr) > 0:
    if arr.pop() != pointer1.data
        return False
12. return True
'''

# Definition of LL
class LinkedList:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class Solution:
    def isPalindrome(self, head):
        
        if not self.head:
            return False
        if self.head.next == None:
            return True
        
        arr = []

        pointer1 = self.head
        pointer2 = self.head.next

        while pointer2.next != None:
            arr.append(pointer1.data)

            pointer1 = pointer1.next
            arr.append(pointer1.data)

            pointer2 = pointer2.next
            pointer2 = pointer2.next

        if len(arr) * 2) != 0:
            arr.pop()

        while len(arr) > 0:
            if arr.pop() != pointer1.data:
                return False
        else:
            return True