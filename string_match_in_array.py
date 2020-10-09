


def match( words ):

    arr = []

    for i,word in enumerate(words):
        for j,elem in enumerate(words):
            if word == elem:
                print(word)
                continue
            else:
                if word in elem and word not in arr:
                    arr.append(word)

    return arr

print(match(["leetcoder","leetcode","od","hamlet","am"]))