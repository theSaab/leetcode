


# # arr nums[int]
# # running sum 
# # non empty
# # non infinite
# # return arr[int] 
# # input [1,2,3,4]
# # ex: [1,3,6,10]

# # 1. empty arr[]
# # 2. for i,element in enum(nums)
# # 3. try: new_num = arr[i-1] + element
# # 4. except: new_num = element
# # 5. arr.append(new_num)
# # 6. return arr

# # 1. for i,element in enum(nums)
# # 2. try: nums[i] = nums[i-1] + nums[i]
# # 3. except: nums[i] = nums[i]
# # 4. return nums

# def running_sum(nums):

#     for i in range(1,len(nums)):
#         nums[i] = nums[i] + nums[ i - 1 ]
    
#     return nums

# # input [1,2,3,4]
# # ex: [1,3,6,10]
# print(running_sum([1,2,3,4]))















