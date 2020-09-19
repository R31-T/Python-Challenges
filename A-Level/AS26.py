punctuation = [',','.',':',';','!','/','?',' ']
letters = []
word = ''
wordlist = []

text = input('Enter the text: ')

for i in range(len(text)):
    if text[i] not in punctuation:
        letters.append(text[i])
    
    elif text[i] in punctuation and text[i-1] in punctuation:
        c = 0
    
    else:
        word = ''.join(letters)
        wordlist.append(word)
        letters = []

totalcharacters = 0
for i in range(len(wordlist)):
    totalcharacters = totalcharacters + len(wordlist[i])

print('Average word length:',totalcharacters/len(wordlist))