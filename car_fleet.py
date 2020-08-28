

def fleet(target, position, speed):

    if len(position) == 0:
        return 0
    
    else:
        enum_pos = {}
        
        for i,pos in enumerate(position):
            enum_pos[pos] = speed[i]
        
        fleet_num = 0
        position.sort()
  
        for i,node in enumerate(position):
            try:
                if enum_pos[node] <= enum_pos[position[i+1]]:
                    fleet_num += 1
                else:
                    print('rthtewas')
            except:
                fleet_num += 1
        # else:
            
        return fleet_num

print(fleet(10, [6,8], [3,2]))

[0,3,5,8,10]