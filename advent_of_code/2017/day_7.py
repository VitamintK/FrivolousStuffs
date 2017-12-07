mapp = dict()
weights = dict()
while True:
    try:
        s = input().split()
        mapp[s[0]] = []

        if len(s) > 2:
            nots = [x.strip(',') for x in s[3:]]
            for i in nots:
                mapp[s[0]].append(i)
        weights[s[0]] = int(s[1][1:-1])
    except Exception as e:
        #raise e
        break

def dfs(i):
    weight = []
    for j in mapp[i]:
        weight.append(dfs(j))
    if len(set(weight)) > 1:
        print(weight)
        print([weights[x] for x in mapp[i]]) 
    return sum(weight) + weights[i]
dfs('azqje')
