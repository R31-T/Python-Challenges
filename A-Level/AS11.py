#Create a pass phrase generator that helps students to create secure passwords. Bonus 50 if it uses an external file
import random
caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nocaps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

password = []

while True:
    length = int(input('How many characters? '))
    if length >= 8:
        break
    print('Password too short')

truelength = length - 1

password.append(random.choice(caps))

for i in range(int(truelength/2)):
    password.append(random.choice(nocaps))

for i in range(truelength-int(truelength/2)):
    password.append(random.choice(numbers))

print('Password:',''.join(password))