 
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

level = [1,8,6,2,5,4,8,3,7]

def water(levels):

    count = 0
    volume = 0
    taller_point = levels[0]
    shorter_point = 0
    for element in levels[1:]:
        space = 1

        if element > taller_point:
            shorter_point = taller_point
            taller_point = element
            if space * shorter_point > volume:
                
            space = 1
        else:
            space += 1
        if space *   


    #     left_point = element
    #     for element in levels[count + 1:]:
    #         space += 1
    #         if element > left_point:
    #             base = left_point
    #         else:
    #             base = element 
    #         if (base * space) > volume:
    #             volume = base * space
    #         else: 
    #             continue 
    #     else:
    #         count += 1
    # else:
    #     print(volume)

water(level)
