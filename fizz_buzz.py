''' Fizz Buzz
Write a method fizz_buzz(max) that takes in a number max and returns an array containing all numbers greater than 0 
and less than max that are divisible by either 4 or 6, but not both '''

array = []

def fizz_buzz():
    max = int(input('Please enter a number of your choice: '))
    for i in range(max):
        if i%4 == 0 and i%6 == 0:
            print()
        elif i % 4 == 0 or i % 6 == 0:
            array.append(i)
    print(array)

fizz_buzz()