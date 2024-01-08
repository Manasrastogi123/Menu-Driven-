import math

def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

def divide_numbers():
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

def power():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is: {result}")

def find_maximum():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    max_num = max(num1, num2)
    print(f"The maximum of {num1} and {num2} is: {max_num}")

def find_minimum():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    min_num = min(num1, num2)
    print(f"The minimum of {num1} and {num2} is: {min_num}")

def calculate_average():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    average = (num1 + num2) / 2
    print(f"The average of {num1} and {num2} is: {average}")

def calculate_remainder():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        remainder = num1 % num2
        print(f"The remainder of {num1} divided by {num2} is: {remainder}")

def calculate_square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        result = math.sqrt(num)
        print(f"The square root of {num} is: {result}")

def calculate_cubert():
    num = float(input("Enter a number: "))
    result = num**(1/3)
    print(f"The cube root of {num} is: {result}")

def calculate_percentage():
    num = float(input("Enter the total: "))
    percentage = float(input("Enter the percentage to calculate: "))
    result = (percentage / 100) * num
    print(f"{percentage}% of {num} is: {result}")

def calculate_factorial():
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        result = math.factorial(num)
        print(f"The factorial of {num} is: {result}")

def calculate_average_of_list():
    num_list = input("Enter a list of numbers separated by commas (e.g., 1,2,3): ")
    num_list = [float(num) for num in num_list.split(',')]
    if not num_list:
        print("Error: Empty list. Please enter at least one number.")
    else:
        average = sum(num_list) / len(num_list)
        print(f"The average of the numbers is: {average}")

def calculate_area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius**2
    print(f"The area of the circle with radius {radius} is: {area}")

def convert_temperature():
    temperature = float(input("Enter the temperature in Celsius: "))
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature} Celsius is equivalent to {converted_temperature} Fahrenheit")

def check_prime_number():
    num = int(input("Enter a positive integer: "))
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")

# Example menu loop:
while True:
    print("\nMenu:")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Multiply Numbers")
    print("4. Divide Numbers")
    print("5. Power")
    print("6. Find Maximum")
    print("7. Find Minimum")
    print("8. Calculate Average")
    print("9. Calculate Remainder")
    print("10. Calculate Square Root")
    print("11. Calculate Cube Root")
    print("12. Calculate Percentage")
    print("13. Calculate Factorial")
    print("14. Calculate Average of List")
    print("15. Calculate Area of Circle")
    print("16. Convert Temperature")
    print("17. Check Prime Number")
    print("18. Quit")

    choice = input("Enter your choice (1-18): ")

    if choice == '1':
        add_numbers()
    elif choice == '2':
        subtract_numbers()
    elif choice == '3':
        multiply_numbers()
    elif choice == '4':
        divide_numbers()
    elif choice == '5':
        power()
    elif choice == '6':
        find_maximum()
    elif choice == '7':
        find_minimum()
    elif choice == '8':
        calculate_average()
    elif choice == '9':
        calculate_remainder()
    elif choice == '10':
        calculate_square_root()
    elif choice == '11':
        calculate_cubert()
    elif choice == '12':
        calculate_percentage()
    elif choice == '13':
        calculate_factorial()
    elif choice == '14':
        calculate_average_of_list()
    elif choice == '15':
        calculate_area_of_circle()
    elif choice == '16':
        convert_temperature()
    elif choice == '17':
        check_prime_number()
    elif choice == '18':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 18.")