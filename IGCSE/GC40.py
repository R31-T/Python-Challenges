#During exercise, you need to train at a pace and intensity where your heart rate increases,
#but not exceeds, 70% - 75% of your theoretical maximum heart rate (TMHR).
#Calculate this using the follow formula.MHR = 70 % x (225 minus your age).

age = int(input('Age: '))
hr = int(input('Heart rate (BPM): '))

mhr = 0.7*(225-age)

print('Max heart rate:',mhr)