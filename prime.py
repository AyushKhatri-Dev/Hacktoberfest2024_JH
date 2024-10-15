# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # Prime numbers must be greater than 1
    for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:
            return False
    return True

# Take user input
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
