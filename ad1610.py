print("This python script adds. subtracts, multiplies and divides numbers")
print("\nSelect an operation:")
print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n")
print("4. Division\n")

choice = input("Enter your choice (1-4): ")

if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid choice. Please select a valid option (1-4).")
