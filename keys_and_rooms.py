

def doors(rooms):

    lst_keys = [0]
    for keys in rooms[0]:
        if keys not in lst_keys:
                lst_keys.append(keys)

    for i in range(len(rooms)):
        
        for i,element in enumerate(rooms):
            # print(lst_keys)
            # print(i )
            if i not in lst_keys:
                print(i)
                continue
            else:
                for num in element:
                    if num not in lst_keys:
                        lst_keys.append(num)
  
    print(lst_keys)
    if len(lst_keys) != len(rooms):
            return False
    else:
        return True


print(doors([[1,1],[]]))
