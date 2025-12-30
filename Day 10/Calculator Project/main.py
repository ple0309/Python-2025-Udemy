from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# print(operation["*"](4,8))

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
