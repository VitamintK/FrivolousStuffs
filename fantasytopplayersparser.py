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

def espn_to_excel(ostr):
    for line in ostr.split('\n'):
        splits = line.split('	')
        splits[0] = alphanumeric_space(splits[0])
        yield '	'.join([de_espn(splits[0])]+splits[2:3]+splits[5:13])

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
