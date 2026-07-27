# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def sum(user_list):
    sum = 0
    for i in user_list:
        sum =+ i
    return sum

def average(user_list):
    num = len(user_list)
    add = sum(user_list)
    avg = add / num
    return avg

def minimum(user_list):
    least = 0
    for i in user_list:
        if i < least:
            least = i
    return least

def maximum(user_list):
    large = 0
    for i in user_list:
        if i > large:
            large = i
    return large

def main():
    count = int(input("How many numbers? "))
    numbers = []
    for i in range(count):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    print("---Results---")
    addition = sum(numbers)
    print(f"Sum: {addition}")
    mean = average(numbers)
    print(f"Average: {mean}")
    least = minimum(numbers)
    large = maximum(numbers)
    print(f"Minimum: {least} \nMaximum: {large}")


if __name__ == "__main__":
    main()