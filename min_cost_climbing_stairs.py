

def stairs(cost):

    price = 0
    if cost[0] < cost[1]:
        price += cost[0]
        i = 0
        while i < len(cost):
            try:

                if cost[ i + 1 ] == cost[ i + 2 ]:
                    price += cost[ i + 2]
                    i += 2

                elif cost[ i + 1 ] < cost[ i + 2 ]:
                    price += cost[ i + 1 ]
                    i += 1
                    

                else:
                    price += cost[i + 2]
                    i += 2
            
            except:
                break

    else:
        price += cost[1]
        i = 1
        while i < len(cost)-1:
            try:
                if cost[ i + 1 ] == cost[ i + 2 ]:
                    price += cost[ i + 2]
                    i += 2

                elif cost[ i + 1 ] < cost[ i + 2 ]:
                    price += cost[ i + 1 ]
                    i += 1

                else:
                    price += cost[i + 2]
                    i += 2
            
            except:
                break

    return price

print(stairs([0,1,2,2]))