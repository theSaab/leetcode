

nums = [1,2,3,4,5,6,7]
k = 3

def rotate(list, degree):

    for i in range(degree):
        list.insert(0, list.pop())
        
    print(list)

rotate(nums, k)