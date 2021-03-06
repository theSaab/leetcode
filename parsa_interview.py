


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

# # Definition of LL
# class LinkedList:
#     def __init__(self, data = 0, next = None):
#         self.data = data
#         self.next = next

# class Solution:
#     def isPalindrome(self, head):
        
#         if not self.head:
#             return False
#         if self.head.next == None:
#             return True
        
#         arr = []

#         pointer1 = self.head
#         pointer2 = self.head.next

#         while pointer2.next != None:
#             arr.append(pointer1.data)

#             pointer1 = pointer1.next
#             arr.append(pointer1.data)

#             pointer2 = pointer2.next
#             pointer2 = pointer2.next

#         if len(arr) * 2) != 0:
#             arr.pop()

#         while len(arr) > 0:
#             if arr.pop() != pointer1.data:
#                 return False
#         else:
#             return True



'''
input: int hours, minutes
return smaller angle between hands
return int 
hours => [0, 12[
minutes => [0, 60[
ex: 2, 19

hours: 1 hour = 30 degrees
minutes: 1 minute = 6 degrees

1. Translate both inputs to degrees
1.5 transform hours to double, add minutes/60
2. take abs(difference between both)
3. return smallest int 

[3.25, 15]

97.5
90

'''


# def angleBetweenHands( hour, minute):

#     angleMinutes = minute%60 * 6
#     angleHour = (hour + minute%60/60) * 30

#     angle = abs(angleHour%12 - angleMinutes)
#     if (360 - angle < angle):
#         return (360-angle)
#     return angle


# print(angleBetweenHands( 12, 30))


'''

given a paragraph and list of banned words
return most frequent not banned word
para can be empty
banned can be empty
no nums 
input: para(str), banned(list(str))
return word(str)
answer is unique
space is seperation

'''

# 1. dik = {}
# 1.5 word = ''
# 2. for char in para:
# 3.      if char != ' ':
# 4.           word = word + char
#         else:
#             if word not in dik and word not in banned:
#                 dik{word} = 1
#                 word = ''
#             elif word not in banned :
#                 dik{word} += 1
#                 word = ''
# 5. max = 0
# 5.5 word =''
# 6. for node in dik:
# 7. if dik{node} > max :
#     max = dik{node}
#     word = node
# 8. return word

                
# def mostCommon(paragraph, banned):
#     dik = {}
#     word = ''
#     alpha = 'abcdefghijklmnopqrstuvwxyz'

#     for char in paragraph:
#         print(word)
#         if char.lower() in alpha:
#             word = word + char
#         elif word != '':
#             word = word.lower()
#             if word not in dik and word not in banned:
#                 dik[word] = 1
#                 word = ''
#             elif word in dik:
#                 print('faefawfaw')
#                 dik[word] += 1
#                 word = ''
#             else:
#                 word = ''
#     else:
#         if word != '':
#             dik[word.lower()] = 1
            
#     max = 0
#     word = ''
#     for node in dik:
#         if dik[node] > max :
#             max = dik[node]
#             word = node
#     print(dik)
#     return word

# print(mostCommon("Bob. hIt, baLl", ["bob", "hit"]))


def somme( num ):

    if num == 0:
        return None

    else:

        i = 1
        somme = 0 
        while i <= abs(num):

            if abs(num) % i == 0 and i % 2 != 0:
                somme += i
            
            i += 1
    
    return somme

print(somme(-2001))












