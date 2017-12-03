import random
l = []
while len(l) < 10 or list(sorted(l[-10:])) != l[-10:] or len(set(l[-10:]))!=10:
    l.append(random.randint(0,10))

print(l[-10:])
