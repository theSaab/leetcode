


def validWord(words, chars):

    s = ''

    for word in words:

        for char in word:
            # print(word)
            # print(char)

            if word.count(char) <= chars.count(char):
                # print('here')
                continue
            else:
                # print('fvsefs')
                break

        else:
            s += word

    return len(s)


print(validWord(["cat","bt","hat","tree"], "atach"))