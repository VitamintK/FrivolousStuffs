with open('cipher4.txt', encoding="utf8") as f:
    p = f.read()
#for i in range(-26,26):
#    print(''.join([chr(ord(c)+i) for c in p]))
from collections import defaultdict
p = p[1:] #get rid of initial nonbreaking space
p = p[:-1]#get rid of trailing newline char
print(p)
d = defaultdict(int)
for i in range(len(p)):
    print(ord(p[i]))
    d[ord(p[i])]+=1
print(sorted(d.items(), key = lambda x: x[1]))

ngram_2 = defaultdict(int)
for i in range(len(p)-1):
    ngram_2[(ord(p[i]), ord(p[i+1]))]+=1
print(sorted(ngram_2.items(), key= lambda x: x[1]))

print(len(d))

#subst = {143: ' ', 163: 'e', 142: 'a', 119: 't', 89: 'c', 212: 'k', 52: 'r',
#         216:'h', 191: 's', 167: 'i', 74: 'l', 206: 'p', 2: 'b', 245: 'o',
#         59: 'u', 247: 'm', 249: 'n', 184: 'g', 157: 'f', 185: 'y', 29: 'q',
#         140: 'w', 123: 'd', 192: '.', 125: 'H', 209: 'B'}

for xor in range(256):
    string = ''
    for i in p:
    #if ord(i) in subst:
    #    string+=subst[ord(i)]
    #else:
    #    string+=','+str(ord(i))+','
        string+=chr(ord(i)^xor)
        
    print(string)
