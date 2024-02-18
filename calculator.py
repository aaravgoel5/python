import math

class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    def square_root(self, num):
        if num < 0:
            return "Error: Cannot calculate square root of a negative number"
        return math.sqrt(num)


def main():
    calculator = Calculator()

    print("Welcome to Simple Calculator App!")

    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.add(num1, num2)
            print(f"Result: {result}")
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == "4":
            num1 = float(input("Enter dividend: "))
            num2 = float(input("Enter divisor: "))
            result = calculator.divide(num1, num2)
            print(f"Result: {result}")
        elif choice == "5":
            num = float(input("Enter a number: "))
            result = calculator.square_root(num)
            print(f"Square root: {result}")
        elif choice == "6":
            print("\nExiting Calculator App. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose again.")


if __name__ == "__main__":
    main()
