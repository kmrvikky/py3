numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

largest_number = max(numbers)
print("The largest number is:", largest_number)
