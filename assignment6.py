# 1. Print numbers from 1 to 10 using a for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Print numbers from 20 to 1 using a while loop
print("Numbers from 20 to 1:")
num = 20
while num > 0:
    print(num, end=" ")
    num -= 1
print("\n")

# 3. Print even numbers from 1 to 10
print("Even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# 4. Print numbers from 1 to n
n = int(input("Enter a number (n): "))
print(f"Numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")

# 5. Print all odd numbers between 1 and n
n = int(input("Enter a number (n): "))
print(f"Odd numbers from 1 to {n}:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print("\n")
# 6. Print 'Happy Birthday!' five times
print("Happy Birthday! (5 times):")
for _ in range(5):
    print("Happy Birthday!")
print("\n")

# 7. Print first n terms of series of squares
n = int(input("Enter a number: "))
print(f"The first {n} terms of the series are:")
for i in range(1, n + 1):
    print(i**2, end=" ")
print("\n")

# 8. Print multiplication table of a number
n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("\n")

# 9. Print first 8 terms of an arithmetic progression
print("First 8 terms of the arithmetic progression (starting at 3, common difference 4):")
start = 3
difference = 4
for i in range(8):
    print(start + i * difference, end=" ")
print("\n")

# 10. Print first 6 terms of a geometric progression
print("First 6 terms of the geometric progression (starting at 2, common ratio 3):")
start = 2
ratio = 3
term = start
for _ in range(6):
    print(term, end=" ")
    term *= ratio
print("\n")
# 11. Calculate sum of integers from 1 to n
n = int(input("Enter a positive integer: "))
sum_integers = sum(range(1, n + 1))
print(f"Sum of integers from 1 to {n} is: {sum_integers}")
print("\n")

# 12. Calculate sum of reciprocals from 1 to n
n = int(input("Enter a positive integer: "))
sum_reciprocals = sum(1 / i for i in range(1, n + 1))
print(f"Sum of reciprocals from 1 to {n} is: {sum_reciprocals:.2f}")
print("\n")

# 13. Accumulate numbers entered 5 times
total = 0
print("Enter 5 numbers:")
for _ in range(5):
    num = int(input())
    total += num
print(f"The final running total is: {total}")
print("\n")

# 14. Calculate factorial of a number
n = int(input("Enter a positive integer to calculate its factorial: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
print("\n")

# 15. Calculate power of base to exponent without ** or math.pow()
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1
if exponent > 0:
exponent > 0:
    for _ in range(exponent):
        result *= base
elif exponent < 0:
    for _ in range(-exponent):
        result /= base
print(f"The result of {base}^{exponent} is: {result}")