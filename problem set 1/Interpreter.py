def main():

    mathExpression = input("Expression: ")
    mathInterpreter(mathExpression)


def mathInterpreter(expression):
    expression = expression.strip().split()
    lst = ["+", "-", "*", "/"]
    if len(expression) != 3:
        print("Invalid input")
    elif expression[1] not in lst:
        print("Invalid input")
    else:
        x = float(expression[0])
        y = float(expression[-1])
        if expression[1] == "+":
            print(x + y)
        elif expression[1] == "-":
            print(x - y)
        elif expression[1] == "*":
            print(x * y)
        elif expression[1] == "/":
            if y == 0:
                print("Cannot divide by zero")
            else:
                print(x / y)
main()