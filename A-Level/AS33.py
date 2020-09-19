#Create a Hex & Binary Quiz machine
import random

hexvalues = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']
binaryvalues = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
hexdict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101' , 'E': '1110', 'F': '1111'} 
binarydict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A','1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
questions = []
correctanswers = []
incorrectanswerposition = []
answers = []

while True:
    print('Hex to binary [A]')
    print('Binary to hex [B]')
    
    quiztype = input('A or B: ')
    if quiztype in ['A','B']:
        break
        
    print('Invalid input!')

numberofquestions = int(input('Number of questions: '))

if quiztype == 'A':
    print(numberofquestions,'questions on hex to binary.')
    for i in range(numberofquestions):
        hexsplit = []
        binarysplit = []
        for a in range(2):
            hexsplit.append(random.choice(hexvalues))
            binarysplit.append(hexdict[hexsplit[a]])
            
        hexvalue = ''.join(hexsplit)
        binaryanswer = ''.join(binarysplit)
        
        questions.append(hexvalue)
        correctanswers.append(binaryanswer)
        
        print('Hex value:',hexvalue)
        answer = input('Enter the binary value: ')
        
        answers.append(answer)
        
        if answer != binaryanswer:
            incorrectanswerposition.append(i)

else:
    print(numberofquestions,'questions on binary to hex.')
    for i in range(numberofquestions):
        binarysplit = []
        hexsplit = []
        for a in range(2):
            binarysplit.append(random.choice(binaryvalues))
            hexsplit.append(binarydict[binarysplit[a]])
            
        binaryvalue = ''.join(binarysplit)
        hexanswer = ''.join(hexsplit)
        
        questions.append(binaryvalue)
        correctanswers.append(hexanswer)
        
        print('Binary value:',binaryvalue)
        answer = input('Enter the hex value: ')
        
        answers.append(answer)
        
        if answer != hexanswer:
            incorrectanswerposition.append(i)

print('Quiz complete!')
print('Score:',numberofquestions - len(incorrectanswerposition),'out of',numberofquestions)

if len(incorrectanswerposition) == 0:
    print('All correct!')
    
else:
    print('Corrections!')
    
    for i in range(len(incorrectanswerposition)):
        print('Value:',questions[incorrectanswerposition[i]])
        print('Your answer:',answers[incorrectanswerposition[i]])
        print('Correct answer:',correctanswers[incorrectanswerposition[i]])
        print('     ')