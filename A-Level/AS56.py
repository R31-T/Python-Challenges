import random
c = 0
for i in range(5):
    bn = []
    tc = []
    for i in range(8):
        bn.append(random.randint(0,1))

    for i in range(8):
        if bn[i] == 0:
            tc.append(1)
        if bn[i] == 1:
            tc.append(0)

    tc[7] = tc[7] + 1

    for i in range(7):
        if tc[7-i] == 2:
            tc[7-i] = 0
            tc[(6-i)] = tc[(6-i)] + 1
            
    if tc[0] == 2:
        tc[0] = 1
        tc.append(0)
        print('Overflow')
    
    for i in range(len(bn)):
        bn[i] = str(bn[i])
        
    for i in range(len(tc)):
        tc[i] = str(tc[i])
        
    binary = ''.join(bn)
    
    print('Binary number:',binary)
    answer = input('Answer: ')
    
    
    if answer == ''.join(tc):
        c = c + 1
    
print('Score:',c,'/ 10')