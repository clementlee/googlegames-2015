words = []
with open('wordlist') as asdf:
    words = [i.lower().rstrip() for i in asdf.readlines()]

lol = []
with open('cypher') as asdf:
    lol = list(asdf.readline().rstrip())

import random
def shuffle(string):
    for i in xrange(len(string)):
        i1 = random.randint(0, len(string)-1)
        i2 = random.randint(0, len(string)-1)
        t = string[i1]
        string[i1] = string[i2]
        string[i2] = t
    return string



alphabak = list('abcdefghijklmnopqrztuvwxyz')
alpha = alphabak

def substitute(alpha):
    newlol = [' '] * len(lol)
    for i in xrange(len(lol)):
        if lol[i] is ' ':
            continue
        else:
            newlol[i] = alpha[ord(lol[i])-ord('A')]

    return newlol



def done(alpha):
    newlol = (''.join(substitute(alpha))).split()
    for word in newlol:
        if word not in words:
            return False

    return True


i = 0
while not done(alpha):

    alpha = shuffle(alpha)
    i += 1
    if i % 1000 is 0:
        print i

print substitute(alpha)




