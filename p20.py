probs = []
with open('probabilities') as pfile:
    probs = [int(float(i.rstrip())*10000000) for i in pfile.readlines()]

print probs
print sum(probs)

import random
def gennum():
    newnum = random.randint(0, 10000000)
    for i in xrange(len(probs)):
        if newnum < probs[i]:
            return i
        else:
            newnum -= probs[i]
    return len(probs) -1

def trial():
    i = 0
    arr = [False]* len(probs)
    while not all(arr):
        n = gennum()
        arr[n] = True
        i += 1
    return i

trials = [trial() for i in xrange(1000000)]
print sum(trials)/(len(trials)*1.0)
