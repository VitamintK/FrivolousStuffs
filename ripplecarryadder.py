

#! /usr/bin/env python
#
# The beginnings of the ripple-carry adder simulation for
# CS 52, Assignment 5.
#
# Kevin Wang
# Friday 18 October 2013
#
#

#
# The fundamental classes are Node and Gate.
#
class Node :

    """A Node is a junction. (Think of a gate as having wires for input
    and output; a node is where the wires are connected.) A node
    maintains its current value, a bit, and a list of all gate
    whose inputs are connected to that node. There are three methods:
    getState  which returns the current bit value,  setState
    which changes the state and, if necessary, calls  notify  for all
    the gates in the input list, and  connect  which adds a gate to
    the notification list."""

    def __init__(self, sta = 0) :
        """Create a node."""
        self.state = sta
        self.notifyList = []
        
    def setState(self, newstate) :
        """Update the state of the node."""
        if self.state != newstate :
            self.state=newstate
            for gate in self.notifyList:
                gate.notify()
                
    def getState(self) :
        """Return the state of the node."""
        return self.state

    def connect(self, gate) :
        """Add a gate to the notification list."""
        self.notifyList.append(gate)


class Gate :

    """A Gate has some input nodes, one output node, and two important
    methods. One is  evaluate  which--when defined in a subclass---
    reads the input nodes and returns the value appropriate for that
    gate. The other is  notify  which obtains the resulting value for
    the current inputs and, if necessary, sets the output node to the
    correct value."""
    

    def __init__(self, inputs, output) :
        """Create a gate."""
        self.outState = output
        self.inStates = inputs
        for inp in inputs :
            inp.connect(self)
        self.outState.setState(self.evaluate())

    def evaluate(self) :
        """Evaluate the result of the gate."""
        pass

    def notify(self) :
        """Respond to a notification by changing the output state, if
         necessary."""
        newOutState = self.evaluate()
        if newOutState != self.outState.getState() :
           self.outState.setState(newOutState)


#
# Gate1 and Gate2 are specializations in which a gate is described with
# either one or two input nodes, rather than an arbitrary list of them.
#
class Gate1 :
    
    def __init__(self, input, output) :
        """Create a gate with only one input node."""
        Gate.__init__(self, [input], output)

class Gate2 :
    
    def __init__(self, input0, input1, output) :
        """Create a gate with only two input nodes."""
        Gate.__init__(self, [input0,input1], output)


#
# Here we create the AndGate and the AndGate2. Notice that no new code
# is necessary for AndGate2.
#
class AndGate(Gate) :
    
    def evaluate(self) :
        """Evaluate the logical-and of the input nodes."""
        for inp in self.inStates :
            if inp.getState() == 0 : return 0
        return 1

class AndGate2(Gate2, AndGate) : pass


#
# Here we create NotGate1. There is no sensible way to define a not-gate
# with more than one input.
#
class NotGate1(Gate1, Gate) :
    
    def evaluate(self) :
        inp = self.inStates[0]
        if inp.getState() != 0 : return 0
        else :                   return 1


#
# Put your solutions below this line. Change nothing above it, except to
# insert your name and the current date.
#


class OrGate(Gate) :
    """An OrGate's state is 1 if any of the input nodes are 1."""
    def evaluate(self) :
        """Evaluate the logical-and of the input nodes."""
        for inp in self.inStates :
            if inp.getState() == 1 : return 1
        return 0

class OrGate2(Gate2, OrGate) :
    """An OrGate with two input nodes. """
    pass

class XorGate(Gate) :
    
    def evaluate(self) :
        """Evaluate the logical-and of the input nodes."""
        if self.inStates[0].getState() == self.inStates[1].getState(): return 0
        return 1
class XorGate2(Gate2,XorGate):
    pass

class HalfAdder():
    def __init__(self,input0,input1,output0,output1):
        XorGate2(input0,input1,output0)
        AndGate2(input0,input1,output1)

class FullAdder():
    def __init__(self,a,b,c,sum_,carry):
        firstcarry = Node()
        firstsum = Node()
        HalfAdder(a,b,firstsum,firstcarry)
        secondcarry = Node()
        HalfAdder(firstsum,c,sum_,secondcarry)
        OrGate2(firstcarry,secondcarry,carry)

class RippleAdder():
    def __init__(self,inputs0,inputs1,d,sum_,CZNV):
        carryin = Node(d.getState())
        zero = Node()
        zeronot = Node()
        V1 = Node()
        V1not = Node()
        V2 = Node()
        V2not = Node()
        V = Node()
        finalcarry = Node()

        newinputs = []
        curresults = []
        carryouts = [d]
        
        for a,b in zip(inputs0,inputs1):
            carryouts.append(Node())
            newinputs.append(Node())
            curresults.append(Node())
            XorGate2(b,d,newinputs[-1])

            FullAdder(a,newinputs[-1],carryouts[-2],curresults[-1],carryouts[-1])
            #print curresults[-1].getState()
            sum_.append(curresults[-1])

        XorGate2(newinputs[-1],inputs0[-1],V1)
        NotGate1(V1,V1not)
        XorGate2(newinputs[-1],curresults[-1],V2)
        AndGate2(V1not,V2,V)
        XorGate2(carryouts[-1],d,finalcarry)
        
        OrGate(sum_,zero)
        NotGate1(zero,zeronot)
        CZNV.append(finalcarry)
        CZNV.append(zeronot)
        CZNV.append(sum_[-1])
        CZNV.append(V)


def intToBinaryList(k, wordSize = 4):
    #ignore negative integers
    result = []
    for w in range(0,wordSize):
        result.append(k%2)
        k //=2
    return result

def binaryListToInt(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + 2 * (listToInt (lst[1:]))

def binaryListToInt(lst):
    result = 0
    multiplier = 1
    for j in lst:
        result += j * multiplier
        multiplier *=2
    return result

def dub(i):
    return i if i>9 else " "+str(i)

def strify(lst):
    return ''.join([str(i) for i in lst])

def test_the_ripple():
    d = Node(0)
    sum_, CZNV, nodelist0, nodelist1 = [],[],[],[]
    
    word0 = intToBinaryList(0)
    word1 = intToBinaryList(0)
    for o in word0:
        nodelist0.append(Node(o))
    for o in word1:
        nodelist1.append(Node(o))
    RippleAdder(nodelist0,nodelist1,d,sum_,CZNV)
    
    for i in range(0,16):
        word0 = intToBinaryList(i,4)
        for o,p in zip(word0,nodelist0):
            p.setState(o)
        for j in range(0,16):
            word1 = intToBinaryList(j,4)
            for o,p in zip(word1,nodelist1):
                p.setState(o)
            #addition
            d.setState(0)
            sum0 = binaryListToInt([y.getState() for y in sum_])
            CZNV0 = [q.getState() for q in CZNV]
            #subtraction!
            d.setState(1)
            sum1 = binaryListToInt([y.getState() for y in sum_])
            CZNV1 = [q.getState() for q in CZNV]
            print "a={} b={}  sum={},CZNV={}  diff={},CZNV={}".format(
                dub(i),dub(j), dub(sum0), strify(CZNV0), dub(sum1), strify(CZNV1))

        
test_the_ripple()

