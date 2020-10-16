board = []
row1 = []
row2 = []

n = int(input('n: '))
m = int(input('m: '))

#row1,2 (n length)
if n == 1:
    row1.append('.')
    row2.append('*')
    
else:
    for i in range(int(n/2)):
        row1.append('.')
        row1.append('*')
        row2.append('*')
        row2.append('.')
        
    if n%2 == 1:
        row1.append('.')
        row2.append('*')

#column
if m == 1:
    board.append([row1])
    
else:
    for i in range(int(m/2)):
        board.append([row1])
        board.append([row2])
    if m%2 == 1:
        board.append([row1])

for i in board:
    for a in i:
        print(a, end = '')
    print()