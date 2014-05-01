import re
from fantasyaux import *

def alphanumeric(word):
    """cleans everything except letters and numbers and commas and single quotes."""
    return re.sub(r'[^a-zA-Z0-9,\']', '', word)

def alphanumeric_space(word):
    """replaces everything except letters and numbers and commas and single quotes with space."""
    return re.sub(r'[^a-zA-Z0-9,\']', ' ', word)

def de_espn(ostr):
    return alphanumeric_space(ostr.split(',')[0])

def de_espn_printer(olst):
    """take a list in the form of espn and return sanitized names"""
    for line in olst.split("""
"""):
        print de_espn(line)

def espn_to_list(ostr):
    for line in ostr.split('\n'):
        splits = line.split('	')
        yield [de_espn(splits[0])]+splits[2:3]+splits[5:13]

def espn_to_excel(ostr):
    for line in espn_to_list(ostr):
        print '	'.join(line)

def order_espn_to_yahoo(espn):
    """this takes a list in espn format and reorders it to the yahoo ranking order
    also it's probably a REALLY inefficient sorting but I don't know enough
    about sorting algorithm complexity so this will do for now. I think it's
    O(n^2) complexity actually..."""
    for y in yahoo.split('\n'):
        yname = y.split('. ')[1]
        efound=False
        """is there a more pythonic way to recognize when a player in
        the yahoo list isn't in the espn list? Explicit bool (efound)
        seems unpythonic"""
        for e in espn_to_list(espn):
            if  yname == e[0]:
                efound=True
                yield e
        if efound==False:
            yield yname

aggregate = {}
yahooranks = []
i=0
for line in yahoo.split('\n'):
    i+=1
    aggregate[alphanumeric(line.split('.',1)[1])] = i

i=0
for line in espn.split('\n'):
    i+=1
    try:
        yahooranks.append(aggregate[alphanumeric(line.split(',')[0])])
    except:
        yahooranks.append(0)
        #print alphanumeric(line.split(',')[0])
        #print i
    
#for i in yahooranks: print i
for i in range(0,160):
    if i not in yahooranks:
        #print i
        pass
