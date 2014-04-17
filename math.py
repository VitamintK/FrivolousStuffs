"""kevin wang
created to solve the following problem:
Being a mathematician, I found out that my age
seven years ago can be expressed as a sum of consecutive prime numbers.
Not only that, but it can also be expressed as the product of the first
and last numbers of that very same sum.

How old am I now, and when will this phenomenon happen again?"""
def solve_kwok(*args):
    solutions=[]
    for i in range(0,len(args)-1):
        #print "{0}. {1}".format(i,args[i])
        for j in range(i+1,len(args)-1):
            try:
                test=args[i:j]
                if test[0] * test[-1] == sum(test):
                    solutions.append(test)
                    print "{0} age {1}".format(test,test[0]*test[-1])
            except:
                print "{0} {1} is not valid".format(i,j)
    return solutions

#solve_kwok(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
#this is enough to solve the given problem, but for more:

def primes(n):
    """prime number generator from
    http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/
    returns all primes less than or equal to n."""
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
    	if s[i]:
    		j=(m*m-3)/2
    		s[j]=0
    		while j<half:
    			s[j]=0
    			j+=m
    	i=i+1
    	m=2*i+3
    return [2]+[x for x in s if x]

solve_kwok(*primes(100000))
