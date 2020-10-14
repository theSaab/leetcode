



def cross(path):

    origin = [0,0]
    arr = [[0,0]]
    point = [0,0]

    for char in path:
        print(str(point) + ' point')
        print(arr)
        if char == 'N':
            point[1] += 1
            print(point)
        elif char == 'W':
            point[0] -= 1
        elif char == 'S':
            point[1] -= 1
        elif char == 'E':
            point[0] += 1

        x = point
        if x in arr:
            print(point)
            print(arr)
            return True

        arr.append(x)
        
    else:
        return False


# print(cross('NES'))

list = []
bruh = [0,0]
x = bruh
list.append(x)
bruh[0] += 1
list.append(bruh)
print(list)