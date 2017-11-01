print(str(ord(''))+str(ord('')))

print(''.join(map(str,map(ord,''))))

print(''.join([str(ord(x)-ord('a'))for x in 'cabe']))

print('cabe'.translate({ord(b):str(a) for a,b in enumerate('abcdef')}))

