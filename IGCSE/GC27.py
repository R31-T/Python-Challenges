#count from 1 to 20.
#divisible by 3, say "Fizz".
#divisible by 5, say "Buzz".
#both 3 and 5, say "FizzBuzz".
#"1, 2, Fizz, 4, Buzz"...and so forth Let's start by using console.log to print out all of the numbers from 1 and 20.
#But don't type out the numbers in order—find a more awesome way!

i = 0
for i in range(20):
    if (i+1)%3 == 0 and (i+1)%5 != 0:
        print('Fizz')

    if (i+1)%5 == 0 and (i+1)%3 != 0:
        print('Buzz')

    if (i+1)%3 == 0 and (i+1)%5 == 0:
        print('Fizzbuzz')

    if (i+1)%3 != 0 and (i+1)%5 != 0:
        print(i+1)