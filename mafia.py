import random
import math
playeramount = 5
saved = []
copamt = 0
mafamt = 2
medamt = 0
simplelist = copamt+medamt+mafamt

players = []
roleslist = [("player",playeramount-simplelist),
             ("mafia",mafamt),
             ("cop",copamt),
             ("medic",medamt)]
#roleslist[-1] = ("dead",0)
roles = []

civwin = False
mafwin = False

def __init__():
    global saved
    global players
    global roles
    global civwin
    global mafwin
    saved = []
    players = []
    roles = []
    civwin = False
    mafwin = False
    #set dead as -1, players as 0, mafia as 1.
    for i in xrange(0,playeramount):
        players.append(0)
    for i in xrange(0,len(roleslist)):
        roles.extend(setRole(i,[]))
#    print players
def setRole(role,current=[]):
    #recursive setrole
    total = roleslist[role][1]
    if len(current) == total:
        for i in current:
            players[i] = role
        return current
    else:
        ran = random.randint(0,playeramount-1)
        if ran in current or ran in roles:
            return setRole(role,current)
        else:
            current.append(ran)
            return setRole(role,current)
def mafiakill(amt):
    if checkIfMafiaWin():
        print "alldead1"
    else:
        for i in range(0,amt):
            if checkIfMafiaWin() == True:
                break
            ran = random.randint(0,len(players)-1)
            while players[ran]==1 or players[ran] == -1:
                ran = random.randint(0,len(players)-1)
            #print "Person " + str(ran) + ", previously " + str(roleslist[players[ran]][0]) + " was targeted for murder."
            if ran in saved:
                pass
                #print "Person " + str(ran) + ", previously " + str(roleslist[players[ran]][0]) + " was saved by the medic."
            else:
                players[ran] = -1
                #print "Person " + str(ran) + ", previously " + str(roleslist[players[ran]][0]) + " was killed."
def lynch(amt):
    if checkIfCivWin():
        print "alldead1"
    else:
        for i in range(0,amt):
            if checkWins():
                break
            ran = random.randint(0,len(players)-1)
            while players[ran] == -1:
                ran = random.randint(0,len(players)-1)
            #print "Person " + str(ran) + ", previously " + str(roleslist[players[ran]][0]) + " is now dead."
            players[ran] = -1    
def save(amt=1):
    savedl = []
    global saved
    for i in xrange(0,amt):
        if checkWins():
            break
        ran = random.randint(0,len(players)-1)
        while players[ran] == -1 and ran not in savedl:
            ran = random.randint(0,len(players)-1)
        savedl.append(ran)
    saved = savedl
    return savedl
def checkIfMafiaWin():
    for i in players:
        if i !=-1 and i!=1:
            return False
    mafwin = True
    #print "Mafia win"
    return True
def checkIfCivWin():
    for i in players:
        if i!=-1 and i==1:
            return False
    civwin = True
    #print "Civ win"
    return True
def checkWins():
    #output 0 for none, 1 for tie, 2 for civwin, 3 for mafwin
    maftemp = checkIfMafiaWin()
    civtemp = checkIfCivWin()
    if civtemp and maftemp:
        return(1)
        print "Tie"
    elif civtemp:
        #print "Civilian win"
        return(2)
    elif maftemp:
        #print "Mafia win"
        return(3)
    else:
        return(0)
    
def simulation(amt=1):
    civwins = 0
    mafwins = 0
    ties = 0
    data = [0,civwins,mafwins,ties]
    for x in xrange(0,amt):
        __init__()
        while True:
            day()
            a = checkWins()
            if a:
                #print a
                break
            night()
            a = checkWins()
            if a:
                #print a
                break
        data[checkWins()]+=1
    print str(data[2]) + " civilian wins!"
    print str(data[3]) + " mafia wins!"
    print "    " + str(data[1]) + " ties?"
    return (data)
def popsim(samples,persample):
    totaldata = []
    for i in xrange(0,samples):
        simres = simulation(persample)
        totaldata.append(simres)
    return getTotals(totaldata)

def day():
    #print "It is now day."
    lynch(1)
def night():
    #print "It is now night."
    save(1)
    mafiakill(1)

def getTotals(totaldata):
    consolidata = totaldata[0]
    for i in xrange(1,len(totaldata)):
        for j in xrange(0,len(totaldata[i])):
            consolidata[j] += totaldata[i][j]
    return consolidata

#popsim510= popsim(5,20)
#print str(popsim510[2]) + " total civilian wins."
#print str(popsim510[3]) + " total mafia wins."
print playeramount
print simulation(10000)
