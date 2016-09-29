with open('cipher2.txt', encoding="utf8") as f:
    p = f.read()
print(p)
x = 'xw3x3xt3u3t3vx'*10
print(x)
p= p[1:]
#y = ''.join([chr(ord(a)-ord(b)) for a,b in zip(x,p)])
from collections import defaultdict
d = defaultdict(int)
for i in range(len(p)):
#    print(p[i])
#    if(ord(p[i]) == 65279):
#        print("this is the nonbreaking space")
    d[ord(p[i])]+=1
    #print(ord(p[i]), ord(x[i]))
    #print(chr(ord(p[i]) + ord(x[i])))
print(sorted(d.items(), key = lambda x: x[1]))
for i in range(-50,26):
    try:
        string = ''
        for j in p:
            try:
                string+=chr(ord(j)+i)
            except:
                print(ord(j)+i)
        #print(''.join([chr(ord(c)+i) for c in p]))
        print(string)
        print(i)
    except:
        pass
#result:
#In a ceaser cipher you know that a block is only shifted 4 characters. A shift cipher is a generalization where know it can be anything from 1 to n but it is still computed very easy by a computer
