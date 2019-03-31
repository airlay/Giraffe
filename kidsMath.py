import random

l = []
for i in range(30):
    a = random.randint(2, 9)
    # print(a)
    b = 10 - a
    # print(b)
    q = '{} + {} = '.format(a, random.randint(1, b))
    # print(q)

    if q not in l:
        l.append(q)

for x in l:
    print(x)





