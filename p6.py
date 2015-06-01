stocks = []
with open('stocks') as sfile:
    stocks = [i.lower().rstrip() for i in sfile.readlines()]

l = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u':8, 'v': 8, 'w':9, 'x': 9, 'y':9, 'z':9}


def gennum(stock):
    lol = 0
    for letter in stock:
        lol *= 10
        lol += l[letter]

    return lol

print gennum('alle')
u = 0
for i in xrange(len(stocks)):
    lol = gennum(stocks[i])
    match = False
    for j in xrange(len(stocks)):
        if i == j:
            continue
        elif gennum(stocks[j]) == lol:
            match = True
            break

    if not match:
        u += 1

print u

