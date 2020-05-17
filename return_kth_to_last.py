


from collections import deque

input_list = deque('123456')

def kth_to_last(list, kth):

    return(list[-(kth+1)])

kth_to_last(input_list, 2)