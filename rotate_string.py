


def rotate(A, B):

    for i in range(len(A)):
        if B != A:
            B = B[1:] + B[:1]
    
    print(B)
    return A == B


print(rotate("bbbacddceeb", "ceebbbbacdd"))