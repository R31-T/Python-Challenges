import math

def area(r):
    a = math.pi*(r**2)
    return a

def circumference(r):
    c = 2*math.pi*r
    return c
    
r = float(input('Radius: '))

print(area(r))
print(circumference(r))