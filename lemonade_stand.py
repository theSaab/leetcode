

def stand(bills):
  
    spare = []
    for element in bills:
        change = element - 5
        spare.append(element)

        if change != 0:
            if change != 15:
                try:
                    spare.remove(change)
                except:
                    print(change)
                    print(element)
                    print(spare)
                    return False
            else:
                try:
                    try:
                        spare.remove(5)
                        spare.remove(10)
                    except:
                        spare.remove(5)
                        spare.remove(5)
                        spare.remove(5)
                except:
                    print(change)
                    print(element)
                    print('here')
                    print(spare)
                    return False

    else:
        print(spare)
        return True