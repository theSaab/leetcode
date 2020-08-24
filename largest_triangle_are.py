

def triangle(points):

    height = 0 
    width = 0
    for element in points:
        if element[0] > width:
            width = element[0]

        if element[1] > height:
            height = element[1]

    lower_height = height
    lower_width = width

    for element in points:
        if element[0] < width:
            lower_width = element[0]

        if element[1] < height:
            lower_height = element[1]

    width = width - lower_width
    height = height - lower_height

    return width*height/2
    
print(triangle([[0,0],[0,1],[1,0],[0,2],[2,0]]))