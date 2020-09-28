


def bus( distance, start, destination):

    road = 100
    test = 0 

    for element in distance[start:destination+1]:
        test += element
        
    if test < road:
        road = test
    
    test = 0
    
    for i in range(distance.index(start), distance.index(destination), -1):
        test += distance[i]

    if test < road:
        road = test
    
    return road