pk = []
with open('pokemon') as pfile:
    pk = [i.lower().rstrip() for i in pfile.readlines()]

l = {}
for p in pk:
    f = p[0]
    if f not in l:
        l[f] = [p]
    else:
        l[f].append(p)


def maxlen(chain, length):
    last = chain[-1][-1]
    if last not in l:
        return length
    posses = [i for i in l[last] if i not in chain]
    if len(posses) == 0:
        return length

    else:
        return max((maxlen(chain+[i], length+1) for i in posses))


currmax = 0
currp = 'lol'
for p in pk:
    lol = maxlen([p], 1)
    if lol> currmax:
        currmax = lol
        currp = p
    print currmax
    print currp




