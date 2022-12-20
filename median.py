"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
        numbers.sort()
        mid = len(numners) // 2
        res = (numbers[mid] + numbers[~mid]) /2
        print('Median of list: ' + str(res))

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
