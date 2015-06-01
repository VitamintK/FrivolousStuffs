from collections import defaultdict

def tree():
    return defaultdict(tree)

a = 0
treee = tree()
while a < 100:
    treee[a] = tree()
    for i in treee:
        for b in treee:
            treee[a][i][b] = tree()
    a+=1
print(treee)
