''' Doubler
Write a method doubler(numbers) that takes an array of numbers and returns a new array
where every element of the original array is multiplied by 2 '''


numbers = [2, 3, 4, 5, 6]
result = 0
array = []

def doubler():
    for i in numbers:
        result = i * 2
        array.append(result)
    print(array)

doubler()