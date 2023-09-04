number = int(input("Please enter a number: "))

num_str = str(number)

num_of_digits = len(num_str)

smallest_digit = min(num_str)
highest_digit = max(num_str)

print(f"Number of digits in the given number is: {num_of_digits}")
print(f"Smallest number is: {smallest_digit}")
print(f"Highest number is: {highest_digit}")
