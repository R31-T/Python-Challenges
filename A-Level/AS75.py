dtob = {'1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001'}
denary = input('Denary value: ')
bcd = []

for i in range(len(denary)):
    bcd.append(dtob.get(denary[i]))

print(''.join(bcd))