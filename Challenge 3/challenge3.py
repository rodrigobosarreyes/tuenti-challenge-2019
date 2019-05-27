import numpy as np

w, h, f, p = (4, 2, 2, 2)
folds = ('T', 'R')
punches = ((0,0), (2,1))

a = np.zeros((h, w), np.int8)
r = []
for p, x in punches:
    a[x][p] = 1
    # pass
print(a)
print()

# l = [T, L, R, B]
l = [0, 1, 2, 3]

for f in folds:
    if f is 'T':
        # means it's bottom
        a = np.flip(np.flip(a), 1)
    elif f is 'B':
        # means it's top
        np.flip(np.flip(a), 1)
    elif f is 'L':
        # means it's right
        
    elif f is 'R':
        # means it's left
        i = 0
        # Gira a la derecha (Right)
        for d in c:
            a[i] = np.flip(a)
            i += 1
        
print(a)
# tmp = l[2]
# l[2] = l[1]
# l[1] = tmp
b = np.array(l)
    
print('ESTO ES B')
b = b.transpose([1,0,2]).reshape(4, 8)
print(b)

c = np.argwhere(b == 1)
print()
print(c)
print()
# print(np.sort(np.flip(c, 1), axis=1))
print(c[c[:,1].argsort()])
print()
# d = tuple(map(tuple, c))
# print(d)
# print()