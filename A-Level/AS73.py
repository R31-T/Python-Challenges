import random
password = []
special = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/']

password.append(input('Color: '))
password.append(input('Place: '))
password.append(input('Animal: '))

random.shuffle(password)

for i in range(random.randint(4,8)):
    password.append(random.choice(special))

print(''.join(password))