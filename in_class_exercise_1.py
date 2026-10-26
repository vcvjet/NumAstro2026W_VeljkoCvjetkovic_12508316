import numpy as np

# 1. Ask the user to enter three numbers and the name of a star
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
star_name = input("Enter the name of a star: ")

# 2. Store all four values in a list
user_list = [num1, num2, num3, star_name]

# 3. Store the three numbers separately in a NumPy array
numbers_array = np.array([num1, num2, num3])

# 4. Use a for loop to print every item in the list
print("\n--- Items in the list ---")
for item in user_list:
    print(item)

# 5. Read the single number N from a file called limit.txt
try:
    with open("/mnt/c/Users/vcvje/Documents/limit.txt", "r") as file:
        # Read the file content, clean up whitespace, and convert to a number
        N = float(file.read().strip())
except FileNotFoundError:
    print("\nError: The file 'limit.txt' was not found.")
    # Assigning a default value or exiting if the file is missing
    N = None

# 6. Check whether any number in the NumPy array matches N
if N is not None:
    print("\n--- Match Result ---")
    # np.any checks if the condition holds true for at least one element
    if np.any(numbers_array == N):
        print(star_name)
    else:
        print("No match")
