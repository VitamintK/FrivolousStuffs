a = []
while True:
    try:
        a.append([int(x) for x in input().split()])
    except:
        break

ans = 0
for r in a:
    ans += max(r) - min(r)
    print(max(r) - min(r))
print(ans)
