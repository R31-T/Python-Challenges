#HANGMAN
import random

wordlist = ['computer','science','is','the','best','subject']
wordarray = ['','','','','','','','','','','','','','','','','','','','']
hiddenarray = []
lettersguessed = []
x = 0
c = 0

word = random.choice(wordlist)
for i in range(len(word)):
    wordarray[i] = word[i]

for i in range(len(word)):
    hiddenarray.append('_')

print('Word contains',len(word),'letters.')

while True:
    print(hiddenarray)
    guess = input('Guess a letter: ')
    while guess in lettersguessed or len(guess) != 1:
        print('Invalid!')
        guess = input('Guess another letter: ')

    if guess in wordarray:
        for i in range(len(word)):
            if guess == word[i]:
                hiddenarray[i] = guess

    else:
        x = x + 1
    
    lettersguessed.append(guess)
    
    hiddenword = ''.join(hiddenarray)
    
    if hiddenword == word:
        print('Success!')
        print('Number of incorrect guesses:',x)
        break
    
    if x > 4:
        print('Failed!')
        break
        
print('The word is:',word)