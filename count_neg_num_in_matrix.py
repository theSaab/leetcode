



def count( grid ):

    count = 0

    for line in grid:
        for num in line:
            if num < 0:
                count += 1
    
    return count