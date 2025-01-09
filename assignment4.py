# Task 1: Numbers divisible by 7 but not a multiple of 5
def find_numbers():
    result = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
    return ",".join(result)

# Task 2: Calculate value using formula P = √((2 * A * B) / C)
import math
def calculate_p(c_values):
    A = 50
    B = 30
    results = [int(math.sqrt((2 * A * B) / float(c))) for c in c_values]
    return ",".join(map(str, results))

# Task 3: Sort words alphabetically
def sort_words(word_sequence):
    words = word_sequence.split(",")
    return ",".join(sorted(words))

# Task 4: Capitalize all lines
def capitalize_lines(lines):
    return "\n".join(line.upper() for line in lines)

# Task 5: Count vowels in a sentence
def count_vowels(sentence):
    vowels = "aeiou"
    counts = {vowel: sentence.lower().count(vowel) for vowel in vowels}
    return "\n".join(f"{v} appeared {c} times" for v, c in counts.items())

# Task 6: Numbers with all even digits from 1000 to 3000
def even_digit_numbers():
    return [str(i) for i in range(1000, 3001) if all(int(d) % 2 == 0 for d in str(i))]

# Task 7: Check binary numbers divisible by 5
def binary_divisible_by_5(binary_numbers):
    return ",".join(num for num in binary_numbers if int(num, 2) % 5 == 0)

# Task 8: Count letters and digits in a sentence
def count_letters_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return f"LETTERS {letters}\nDIGITS {digits}"

# Example Usage
if __name__ == "__main__":
    # Task 1
    print("Task 1:", find_numbers())

    # Task 2
    c_input = input("Enter C values (comma-separated): ").split(",")
    print("Task 2:", calculate_p(c_input))

    # Task 3
    word_sequence = input("Enter comma-separated words: ")
    print("Task 3:", sort_words(word_sequence))

    # Task 4
    print("Task 4: Enter lines (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print(capitalize_lines(lines))

    # Task 5
    sentence = input("Enter a sentence: ")
    print("Task 5:")
    print(count_vowels(sentence))

    # Task 6
    print("Task 6:", ",".join(even_digit_numbers()))

    # Task 7
    binary_input = input("Enter comma-separated binary numbers: ").split(",")
    print("Task 7:", binary_divisible_by_5(binary_input))

    # Task 8
    sentence = input("Enter a sentence: ")
    print("Task 8:")
    print(count_letters_digits(sentence))
