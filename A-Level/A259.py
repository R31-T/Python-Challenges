import math as m

alist = []
blist = []
nlist = []
elist = []

a = 0
i = 2

e = input('Enter the binomial expression in the form (ax+b)^n: ')

if e[1] == 'x':
    a = 1.0

else:
    alist.append(e[1])
    
    while e[i] != 'x':
        alist.append(e[i])
        i = i + 1

if e[1] == '-' and e[2] == 'x':
    a = -1.0
    i = i + 1

if e[i] == '-':
    blist.append('-')

i = i + 1

while e[i] != ')':
    blist.append(e[i])
    i = i + 1

i = i + 2

while i != len(e):
    nlist.append(e[i])
    i = i + 1

if a != 1.0 and a != -1.0:
    a = float(''.join(alist))

b = float(''.join(blist))
n = int(''.join(nlist))

r=0

while r < n:

    nCr = (m.factorial(n)) / ((m.factorial(r)) * (m.factorial(n - r)))
    anr = a ** (n - r)
    
    if (n - r) == 0:
        xnr = ''
        
    else:
        if (n - r) == 1:
            xnr = 'x'
        else:
            xnr = 'x^' + str(n - r)

    br = b ** r

    if (nCr * anr * br) == 1.0:
        term = str(xnr)

    elif (nCr * anr * br) == -1.0:
        term = str('-' + str(xnr))

    else:
        term = str(nCr * anr * br) + str(xnr)
        
        if term[0] != '-' and r != 0:
            elist.append('+')
            
        if term[0] == '-' and r !=0:
            elist.append('-')
            term = str(-1 * nCr * anr * br) + str(xnr)

    elist.append(term)
    r = r + 1

last = str(b ** n)

if last[0] == '-':
    elist.append('-')
    last = str(-1 * (b ** n))

else:
    elist.append('+')

elist.append(last)

print(' '.join(elist))