class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def subtract(self, num1, num2):
        self.result = num1 - num2

    def multiply(self, num1, num2):
        self.result = num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        self.result = num1 / num2

    def get_result(self):
        return self.result

    def clear(self):
        self.result = 0

def main():
    calculator = Calculator()

    while True:
        print("Input the number of your Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Delete the result")
        print("6. Quit the program")

        user_input = input(": ")

        if user_input == "6":
            break
        elif user_input == "5":
            calculator.clear()
            print("Result cleared.")
        elif user_input in ("1", "2", "3", "4"):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if user_input == "1":
                calculator.add(num1, num2)
                print("Result:", calculator.get_result())
            elif user_input == "2":
                calculator.subtract(num1, num2)
                print("Result:", calculator.get_result())
            elif user_input == "3":
                calculator.multiply(num1, num2)
                print("Result:", calculator.get_result())
            elif user_input == "4":
                result = calculator.divide(num1, num2)
                print("Result:", calculator.get_result())
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print("Result:", calculator.get_result())
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
