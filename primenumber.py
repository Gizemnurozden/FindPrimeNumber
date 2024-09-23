'''

Soru : Girilen bir sayının asal olup olmadığını bulunuz.

'''
number = int(input('Give me a number : '))

prime= True

if number == 1:
    prime = False

for i in range(2,number):
    if (number % i == 0 ):
        prime = False
        break
if prime:
    print('The number is prime')
else:
    print("The number is not prime number")