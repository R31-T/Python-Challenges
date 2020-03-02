import random

a = 0
numberofquestions = int(input('How many questions? '))
paritystring = ''
for i in range(numberofquestions):
    paritylist = []
    paritystring = ''
    for i in range(7):
        paritylist.append(random.choice(['0','1']))

    paritystring = ''.join(paritylist)
    paritybit = random.choice(['0','1'])
    paritylist.append(paritybit)

    print('7-bit parity:',paritystring)
    print('Parity bit:',paritybit)

    c = 0
    for i in range(len(paritylist)):
        if paritylist[i] == '1':
            c = c + 1

    if c%2 == 0:
        paritytype = 'even'
    if c%2 == 1:
        paritytype = 'odd'

    while True:
        parity = input('Parity type = even or odd? ')
        if parity in ['even','odd']:
            break
        print('Invalid input!')

    if parity != paritytype:
        print('Incorrect!')
        print('Parity type:',paritytype)
    else:
        print('Correct!')
        a = a + 1
        
print('Final score:',a,'out of',numberofquestions)