


def smashing(stones):

    while len(stones) > 1:
    
        max = 0
        second_max = 0
        i_max = 0
        i_second = 0
        
        for i,stone in enumerate(stones):
            print(stones)
            print(max)
            print(second_max)
            if stone > max:
                second_max = max
                max = stone
                i_max = i
            elif stone > second_max:
                second_max = stone
                i_second = i
                    
        if max - second_max != 0:
            stones[i_max] = (max - second_max)
            stones.remove(second_max)
        else:
            stones.remove(max)
            stones.remove(second_max)

    return stones
print(smashing([2,7,4,1,8,1]))