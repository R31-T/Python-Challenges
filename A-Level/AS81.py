numbers = [1,2,3,4,5]

def sumandprod(numbers,total = 0,product = 1):
    for i in range(len(numbers)):
        
        total = total + numbers[i]
        product = product*numbers[i]
        
    return total, product

print(sumandprod(numbers))