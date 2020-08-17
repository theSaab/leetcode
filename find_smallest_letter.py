


def find(letters, target):

    letter = 'abcdefghijklmnopqrstuvwxyz'
    target_index = letter.index(target)
    distance = 100
    closest = 'a'

    for element in letters:
        if letter.index(element) > target_index:
            if letter.index(element) - target_index < distance:
                print(letter.index(element) - target_index)
                print(element)
                distance = letter.index(element) - target_index
                closest = element
                print(distance)
                print(str(closest) + ' closest')

    if distance == 100:
        return letters[0]

    else:
        return closest

print(find(["e","e","e","k","q","q","q","v","v","y"]
,"h"))