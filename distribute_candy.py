




def candy( candies, num_people):

    arr = []
    for i in range(num_people):
        arr.append(0)

    count = 1
    while candies > 0 or count < candies:
        
        for i in range(len(arr)):
            print(candies)
            print(count)
            if count < candies:
                arr[i] +=  count
                candies -= count
            else:
                arr[i] += candies
                candies = 0
            count += 1
        
    return arr

print(candy(7, 4))