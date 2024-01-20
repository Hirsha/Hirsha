import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes():
    while True:
        user_input = input("Enter a number (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        try:
            number = int(user_input)
            if number <= 0:
                print("Invalid input. Please enter a positive number.")
                continue
            prime_sum = 0
            for i in range(2, number):
                if is_prime(i):
                    prime_sum += i
            print("Sum of primes smaller than", number, "is:", prime_sum)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

sum_of_primes()