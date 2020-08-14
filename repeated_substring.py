

def repeat(A, B):
    copy = A
    count = 1
    for char in B:
        if char not in A:
            return -1
    else:
        while B not in A :
            if B not in A*2 and len(A) > len(B)*3:
                return -1
            else:
                A += copy 
                count += 1

        return count  

print(repeat("abcabcabcabc", "abac"))