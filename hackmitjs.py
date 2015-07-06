
def even(p):
    g = []
    bit = True
    for k in p:
        if bit:
            g.append(k)
        bit = not bit
    return g

def byte(p):
    return [ord(k) for k in p]

def get_b(p):
    return sum((len(p)-index)*value for index,value in enumerate(p)) % 255
def cksum(p):
    #a=0
    #b=0
    #for k in p:
    #    a=(a+k)%255
    #    b = (b+a)%255
    #return a==sum(p)%255, b==get_b(p)
    a = sum(p)%255
    b = get_b(p)
    #print(a)
    return bin(a << 8 | b)

container = []

def math():
    length=12
    first=0xd06e
    second=0xf00d
    others=0x0000
    print(bin(first))
    #numbers = ['x{}'.format(x) for x in range(12)]
    numbers = list('abcdefghijkl')
    evens = even(numbers)
    firsts = numbers[:length//2]
    seconds = numbers[length//2:]
    i_would_come_up_with_a_name_for_this_data_structure_but_i_cant = [(evens, others), (firsts, first), (seconds, second)]
    print(evens, firsts, seconds)
    def print_b(p):
        return '+'.join(["{}*{}".format(len(p)-index, value) for index,value in enumerate(p)])
    def print_a(p):
        return '+'.join(p)
    for variables, number in i_would_come_up_with_a_name_for_this_data_structure_but_i_cant:
        print("({}) mod 255 ={}".format(print_b(variables), number//(pow(2,8))) + ', ')
        print("({}) mod 255 ={}".format(print_a(variables),(number%256)) + ', ')

    #def brute_force():
    #    actual_numbers = [0 for x in range(12)]
    #    for x in range(256):
    #        pass
            
    def brute_force():
        a=b=c=d=e=f=g=h=i=j=k=l=0
        constraints = []
        for variables, number in i_would_come_up_with_a_name_for_this_data_structure_but_i_cant:
            constraints.append("({}) % 255 =={}".format(print_b(variables), number//(pow(2,8))))
            constraints.append("({}) % 255 =={}".format(print_a(variables), (number%256) ))
        print(constraints)
        for x in constraints:
            print(x)
            print(eval(x))
        for a in range(65,123):
            #break
            for b in range(65,123):
                print('++++')
                for c in range(65,123):
                    for d in range(65,123):
                        for e in range(65,123):
                            print('--------------')
                            for f in range(65,123):
                                print('f',f)
                                for g in range(65,123):
                                    #print('g',g, 'f', f)
                                    for h in range(65,123):
                                        for i in range(65,123):
                                            #print(i)
                                            for j in range(65,123):
                                                for k in range(65,123):
                                                    for l in range(65,123):
                                                        #pass#6*b+5*d+4*f+3*h+2*j+1*l mod 255 =0
                                                        #for x in constraints[-2]:
                                                            #print(x)
                                                        #    j = eval(x)
                                                            #print(j)
                                                         #   if not j:
                                                         #       break
                                                            #print()
                                                        if (5*f+4*g+3*h+2*i+1*j) % 255 ==240 and (f+g+h+i+j) % 255 ==13:
                                                        #else:
                                                            #input("you won")
                                                            print(a,b,c,d,e,f,g,h,i,j)
                                                            container.append([g,h,i,j])
                                                            #input()
        #import itertools
        #for g,i,k in itertools.combinations_with_replacement(range(48,123),3):
        #    for h,jl in itertools.combinations_with_replacement(range(48,123),3):
                
    brute_force()

def tri():
    while True:
        password = input("pass?: ")
        password = byte(password)
        evens = even(password)
        print(cksum(evens))

def wolfram():
    inp = """1	0	0	0	-1	0	0	0	-5	-4	-10	-8	-3928.5
0	1	0	0	0	-1	0	0	4	3	8	6	2854
0	0	1	0	2	0	0	0	7	6	14	12	5563.5
0	0	0	1	0	2	0	0	-6	-5	-12	-10	-4281
0	0	0	0	0	0	1	0	-1	-2	-3	-4	-1187
0	0	0	0	0	0	0	1	2	3	4	5	1427""".split('\n')
    inp = [p.split() for p in inp]
    for i in inp:
        print("{}={}".format('+'.join(['*'.join(x) for x in zip(i[:-1],['x{}'.format(x) for x in range(12)]) if x[0]!='0']), i[-1]) + ',')

def dostuff(numbers):
    print(''.join([chr(int(number)) for number in numbers]))
        
#math()
#wolfram()
n = input('the numbers: ').split()
dostuff(n)
