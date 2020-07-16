


from collections import deque

input_list = deque('125555555553456')

def kth_to_last(list, kth):

    print(list[-(kth+1)])

kth_to_last(input_list, 14)