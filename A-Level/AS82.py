string = 'abcde'

def reverse(string,x = len(string)-1,reverse = []):
    for i in range(len(string)):
        reverse.append(string[x-i])
    
    return reverse
    
print(''.join(reverse(string)))