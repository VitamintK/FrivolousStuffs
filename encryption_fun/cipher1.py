with open('cipher1.txt') as f:
    p = f.read()
for i in range(-26,26):
    print(''.join([chr(ord(c)+i) for c in p]))
#result:
#ThisisjustasimpleceasercipherifyouareabletobreakthisyoucanpassICS31
