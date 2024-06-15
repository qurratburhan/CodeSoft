
def sum(a, b):
    sum  = a+b
    return print("the sum of two numbers is ",int(sum))

def sub(a, b):
    sub1 = a - b
    return print("the difference of two numbers is ", sub1)

def mul(a, b):
    mul1 = a * b
    return print("the product of two numnbers is ", mul1)

def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    result = a / b
    print("The quotient of two numbers is:", result)
    return result

def calculator():
    while True:
        print("\033[1;4;36m------Basic Arithmetic Calculator-------\033[0m")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter the arithmetic operation you want to perform")

        if choice == '5':
            print("Exit")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                sum(a, b)
            elif choice == '2':
                sub(a, b)
            elif choice == '3':
                mul(a, b)
            elif choice == '4':
                div(a, b)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    calculator()


