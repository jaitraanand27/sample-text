import cal as ca


def calculator_info():
    return "Welcome to TP Calculator!"


def addition(a, b):
    return ca.add(a, b)


def subtraction(a, b):
    return ca.subtract(a, b)


def multiplication(a, b):
    return ca.multiply(a, b)


def division(a, b):
    return ca.divide(a, b)


def modulus(a, b):
    return ca.modulus(a, b)


def main():
    print(calculator_info())
    print("=" * 30)

    while True:
        choice = int(input(
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Modulus\n"
            "6. Exit\n"
            "Enter your choice: "
        ))

        match choice:
            case 1:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", addition(a, b))

            case 2:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", subtraction(a, b))

            case 3:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", multiplication(a, b))

            case 4:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = division(a, b)

                if result is False:
                    print("Cannot divide by zero")
                else:
                    print("Result:", result)

            case 5:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = modulus(a, b)

                if result is False:
                    print("Cannot calculate modulus by zero")
                else:
                    print("Result:", result)

            case 6:
                print("Thanks for using TP Calculator!")
                break

            case _:
                print("Invalid choice. Choose between 1 and 6.")


if __name__ == "__main__":
    main()