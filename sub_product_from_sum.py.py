


def transform(num):

    product = 1
    sum = 0
    for char in str(num):
        product *= char
    for char in str(num):
        sum += char
    return product - sum