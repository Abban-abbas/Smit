# 1. Find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 2. Sum all the numbers in a list
def sum_of_list(numbers):
    return sum(numbers)

# 3. Multiply all the numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# 4. Reverse a string
def reverse_string(s):
    return s[::-1]

# 5. Calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 6. Check whether a number falls within a given range
def is_in_range(number, start, end):
    return start <= number <= end

# 7. Count upper and lower case letters in a string
def count_case(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case

# 8. Return a list with distinct elements
def unique_list(lst):
    return list(set(lst))

# 9. Check whether a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 10. Print even numbers from a list
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 11. Check whether a number is perfect
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

# 12. Check whether a string is a palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example Usage
if __name__ == "__main__":
    # Example calls for testing the functions
    print("Max of three:", max_of_three(10, 20, 30))
    print("Sum of list:", sum_of_list([8, 2, 3, 0, 7]))
    print("Product of list:", multiply_list([8, 2, 3, -1, 7]))
    print("Reverse string:", reverse_string("1234abcd"))
    print("Factorial:", factorial(5))
    print("Is in range:", is_in_range(5, 1, 10))
    print("Count case:", count_case("The quick Brow Fox"))
    print("Unique list:", unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
    print("Is prime:", is_prime(11))
    print("Even numbers:", even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("Is perfect:", is_perfect(6))
    print("Is palindrome:", is_palindrome("madam"))
