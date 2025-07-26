''' write a program that prints the number from 1-100.
but for multiples of three print'fizz',instead of number.
for both three and five multiples print'FizzBuzz'
'''
for i in range(1,101):
    if i%3==0 and i%5==0:    
        print("fizz")
    elif i%3==0:
        print("FizzBuzz")
    else:
        print(i)