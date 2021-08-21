""" Write a method average_of_three(num1, num2, num3) that returns the average of three numbers """

def average_of_three(num1, num2, num3):
    avg = (num1 + num2 + num3)//3
    return avg

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(average_of_three(num1, num2, num3))