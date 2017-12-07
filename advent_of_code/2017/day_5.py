a = []
while True:
    try:
        a.append(int(input()))
    except:
        break

b = 0
c = 0
PART2 = True
while True:
    if b %10000 == 0:
        print(b)
    b += 1
    t = a[c]
    if PART2:
        if a[c] > 2:
            a[c] -= 1
        else:
            a[c] += 1
    else:
        a[c] += 1
    c = c + t
    #print(a)
    if c >= len(a) or c < 0:
        break

print(b)
