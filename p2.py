def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

num = '12345'
s = ''
for i in xrange(15):
    s = s + baseN(int(num, 16), 16-i)

print s

import collections
d = collections.defaultdict(int)
for c in s:
    d[c] += 1
a = sorted(d.items(), key=lambda x: x[0], reverse=True)
a = sorted(a, key=lambda x: x[1], reverse=True)

f = ''
for i in xrange(len(a)):
    print a[i]
    f = f + a[i][0]

print f
