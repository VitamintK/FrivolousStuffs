with open("kmrb2tc0.mp3", mode='rb') as f:
    p = f.read()
string = ""
with open("mp3.txt", mode="w") as f2:
    pass
    #for c in p:
    #    try:
    #        f2.write(chr(c))
    #    except:
    #        pass
#spectrogram

s = "J66hZgRy1E0hjRmyzYrN+w38vHDlyxaW8h2jRNnOPdw52CSTw3T9yZosWcDF+iM9zDxmmwTcvUZuJdGMirh30ICenyHLnlfKlrNVi0e4UiyK+9qY/XfiYDiFbDNLa0Cys9BogsAW/IcKtlioSoPHxPFCsn7jDbNEGG/JdHgRkR02x3XB25BX6ECvEHx3kL+S8jNB4lMVyLFaEmPgaEnFsVDGuEFAXl02qrFOBYvWue7jUwdsCuAOn80mBQEyUWQMjWw9ggSrJDma9fRTA/sYa+6t/bBwZ8OlhIj1igAKXNdYQndiETLLmBs7cijFa63tPRdc4kW3gmSFB/mFVizDvw=="
#asd = s[:-4]
#asd = bytes(asd)
#print(asd)
from collections import Counter
c = Counter(s)
print(c)
import base64
b = base64.b64decode(s)
l = [0,0,0,0,0,0,0,0]
for i in b:
    for ind, c in enumerate("{:08b}".format(i)):
        if c == "1":
            l[ind]+=1
print(l)
#for rowlen in range(2,100):
#    count = 0
#    for i in b:
#        print(''.join(["█" if x=="1" else " " for x in "{:08b}".format(i)]), end='')
#        if(count%rowlen == 0):
#            print('')
#        count+=1
keyyy = "mFVizDvw"

keyy = base64.b64decode("asdf")
keyy = [ord(_) for _ in "com"]
g = Counter(b)
print(g)
#for non in range(-60, 60):
if True:
    siu = []
    #for i,j in zip(s[:-2], keyyy*50):
    #    siu.append(ord(i) ^ ord(j))
    for i,j in zip(b, keyy*50):
        siu.append(((i - j)%256 + 256)%256)
    jhis = Counter(siu)
    print(jhis)
    #siu.append(63)
    #siu.append(63)
    #while(len(siu)%4 != 0):
    #    siu.append(63)
    #siu = bytes(siu)
    #for x in siu:
    print(''.join([chr(x) for x in siu]))
#print(siu)
#print([chr(x) for x in base64.b64decode(siu)])
#from Crypto.Cipher import AES
#import base64

#msg_text = 'test some plain text here'.rjust(32)
#secret_key = '1234567890123456' # create new & store somewhere safe

#cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
#encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
#decoded = cipher.decrypt(base64.b64decode(encoded))
#print(decoded.strip())
