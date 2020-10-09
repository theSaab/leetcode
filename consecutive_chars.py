

def consecutive( s ):
    count = 0
    new_count = 0
    for i,char in enumerate(s):
        try:
            if s[i+1] == char:
                new_count += 1
            else:
                if new_count >= count:
                    count = new_count
                new_count = 0
        except:
            if new_count >= count:
                count = new_count
                new_count = 0
            break

    return count+1


print(consecutive('cc'))