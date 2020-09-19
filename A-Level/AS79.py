string = input('String: ')


def make_it_laugh(string,haha = []):
    for i in range(len(string)):
        if string[i] in ['a','e','i','o','u']:
            haha.append('haha')
        else:
            haha.append(string[i])
    
    return(haha)

print(''.join(make_it_laugh(string)))