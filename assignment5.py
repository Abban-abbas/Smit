def alternate_elements():
    lst = input("Enter a list of elements separated by spaces: ").split()
    print("Alternate elements:", lst[::2])

def reverse_list():
    lst = input("Enter a list of elements separated by spaces: ").split()
    reversed_list = lst[::-1]
    print("Reversed list:", reversed_list)

def find_largest():
    lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    print("Largest number:", largest)

def rotate_list():
    lst = input("Enter a list of elements separated by spaces: ").split()
    rotated = lst[1:] + lst[:1]
    print("Rotated list:", rotated)

def delete_word():
    sentence = input("Enter a sentence: ")
    word_to_delete = input("Enter the word to delete: ")
    result = sentence.replace(word_to_delete, "")
    print("Updated sentence:", result)

def format_date():
    date = input("Enter a date in mm/dd/yyyy format: ")
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    mm, dd, yyyy = map(int, date.split('/'))
    print(f"Formatted date: {months[mm - 1]} {dd}, {yyyy}")

def capitalize_words():
    sentence = input("Enter a sentence: ")
    result = ' '.join(word.capitalize() for word in sentence.split())
    print("Capitalized sentence:", result)

def sum_of_rows():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split()))
        matrix.append(row)
    for i, row in enumerate(matrix):
        print(f"Sum of row {i + 1} =", sum(row))

def add_matrices():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the first matrix:")
    matrix1 = [list(map(int, input().split())) for _ in range(rows)]
    print("Enter the second matrix:")
    matrix2 = [list(map(int, input().split())) for _ in range(rows)]
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    print("Sum of matrices:")
    for row in result:
        print(row)

def multiply_matrices():
    rows1 = int(input("Enter the number of rows of the first matrix: "))
    cols1 = int(input("Enter the number of columns of the first matrix: "))
    print("Enter the first matrix:")
    matrix1 = [list(map(int, input().split())) for _ in range(rows1)]
    rows2 = int(input("Enter the number of rows of the second matrix: "))
    cols2 = int(input("Enter the number of columns of the second matrix: "))
    if cols1 != rows2:
        print("Matrix multiplication is not possible.")
        return
    print("Enter the second matrix:")
    matrix2 = [list(map(int, input().split())) for _ in range(rows2)]
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("Product of matrices:")
    for row in result:
        print(row)

# Call each function to test
print("Choose the program to execute:")
options = [
    "Alternate elements of a list",
    "Reverse a list",
    "Find the largest number in a list",
    "Rotate elements of a list",
    "Delete a word from a string",
    "Format a date",
    "Capitalize words in a sentence",
    "Sum of rows in a matrix",
    "Add two matrices",
    "Multiply two matrices"
]
for i, option in enumerate(options, 1):
    print(f"{i}. {option}")
choice = int(input("Enter your choice (1-10): "))

functions = [
    alternate_elements,
    reverse_list,
    find_largest,
    rotate_list,
    delete_word,
    format_date,
    capitalize_words,
    sum_of_rows,
    add_matrices,
    multiply_matrices
]
if 1 <= choice <= 10:
    functions[choice - 1]()
else:
    print("Invalid choice!")
