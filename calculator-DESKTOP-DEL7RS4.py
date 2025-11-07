def calculator():
    """
    Simple calculator with basic arithmetic operations.
    Prompts user for two numbers and an operation choice.
    """
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    try:
        # Get first number from user
        num1 = float(input("Enter the first number: "))

        # Get second number from user
        num2 = float(input("Enter the second number: "))

        # Display operation menu
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        # Get operation choice
        operation = input("\nEnter your choice (1/2/3/4): ").strip()

        # Perform calculation based on choice
        if operation == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif operation == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif operation == '3':
            result = num1 * num2
            print(f"\nResult: {num1} × {num2} = {result}")

        elif operation == '4':
            if num2 == 0:
                print("\nError: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} ÷ {num2} = {result}")

        else:
            print("\nError: Invalid operation choice. Please select 1, 2, 3, or 4.")

    except ValueError:
        print("\nError: Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def main():
    """
    Main function to run the calculator.
    Includes option to perform multiple calculations.
    """
    print("Welcome to the Simple Calculator!")

    while True:
        calculator()

        # Ask if user wants to perform another calculation
        print("\n" + "-" * 40)
        continue_calc = input("Do you want to perform another calculation? (y/n): ").strip().lower()

        if continue_calc not in ['y', 'yes']:
            print("\nThank you for using the Simple Calculator!")
            print("Goodbye!")
            break
        print()  # Add blank line for better readability


if __name__ == "__main__":
    main()