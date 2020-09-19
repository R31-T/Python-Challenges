#list of numbers (for example, a = [5, 10, 15, 20, 25])
#and makes a new list of only the first and last elements of the given list.

numberlist = []
newlist = []

qty = int(input('How many numbers? '))

for i in range(qty):
    numberlist.append(input('Number: '))

newlist.append(numberlist[0])
newlist.append(numberlist[len(numberlist)-1])
print('First and last =',newlist)