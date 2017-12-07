not_root = set()
all_ = set()
while True:
    try:
        s = input().split()
        if len(s) > 2:
            nots = [x.strip(',') for x in s[3:]]
            for i in nots:
                not_root.add(i)
        all_.add(s[0])
    except Exception as e:
        break
print(list(all_ - not_root))
