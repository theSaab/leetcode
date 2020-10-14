

def studying(startTime, endTime, queryTime):

    count = 0

    for i,student in enumerate(startTime):
        if queryTime >= student and queryTime <=   endTime[i]:
            count += 1 

    return count