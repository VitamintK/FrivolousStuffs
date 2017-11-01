#When my two hands are the same, I fall.  When I change one hand from the other, I rise.
#Use me a little bit.

#With two hands, I cannot write.  Neither can I with none.
#Yet still ambidextrous I am, and can write with either one.
#Use me for a bit!
from PIL import Image
im = Image.open("xorclue.png")
width, height = im.size
pix = im.load()
pixelarray = []
for y in range(height):
    for x in range(width):
        pixelarray.append(pix[x,y])

import random
key = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(500*500)]
#key = key * ((height*width + len(key))//len(key))

for i, z in enumerate(zip(key, pixelarray)):
    a,b = z
    pixelarray[i] = (a[0] ^ b[0], a[1] ^ b[1], a[2] ^ b[2])

keyim = Image.new(im.mode, im.size)
keyim.putdata(key)
keyim.save('key.png')

im2 = Image.new(im.mode, im.size)
#print(im2)
im2.putdata(pixelarray)
#print(result)
im2.save('out.png')

#with open('encrypic.png', 'w') as f:
#    f.write(css)

