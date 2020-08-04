

def reverse(list):

    for element in list[::-1]:
        list.append(element)
        list.pop(0)
    return(list)
reverse(["h","e","l","l","o"])
