"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()
        mid = len(numbers) // 2
        if n%2 == 0:
            print (numbers[mid -1] + numbers[mid]) / 2
        else: 
            print numbers[mid]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
