


def place(seats):

    lst = []
    sub = []
    for element in seats:
        if element != 1:
            sub.append(element)
        else:
            lst.append(sub)
            sub = []
    
    long = 0
    spot = None
    for i,element in enumerate(lst):
        
        if len(element) > long:
            long = len(element)
            spot = i
    

    return spot + long//2

    
print(place([1,0,0,0,0,0,1,0,1]))