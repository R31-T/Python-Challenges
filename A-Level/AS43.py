caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nocaps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d = {0:'a',0:'b',0:'c',0:'d',0:'e',0:'f',0:'g',0:'h',0:'i',0:'j',0:'k',0:'l',0:'m',0:'n',0:'o',0:'p',0:'q',0:'r',0:'s',0:'t',0:'u',0:'v',0:'w',0:'x',0:'y',0:'z'}

counter = []
mn = []
mx = []
mxl = []
mnl = []

text = input('Text: ')

for i in range(len(caps)):
    c = 0
    for a in range(len(text)):
        if caps[i] == text[a] or nocaps[i] == text[a]:
            c = c + 1
    x = {c:nocaps[i]}
    d.update(x)
    counter.append(c)

print(d)
print(counter)

for i in range(3):
    mx.append(max(counter))
    mn.append(min(counter))
    counter.remove(max(counter))
    counter.remove(min(counter))

print(mx,mn)

for i in range(3):
    x = d.get(mx[i])
    print(x)
    mxl.append(x)
    
    y = d.get(mn[i])
    print(y)
    mnl.append(y)

print('Most:',mxl)
print('Least:',mnl)