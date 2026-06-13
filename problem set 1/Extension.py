def main():
    '''
    file = input("File name: ")
        print(f"Image/{fileEtenssion(file)}")
        

    def fileEtenssion(filename):
        filename = filename.lower().strip()

        if "." in filename:
            return filename.split(".")[-1]
        else:
            return "None"
    '''
    math = input("Expression: ")
    math = math.split()
    lst = ["+", "-", "*", "/"]

    if len(math) != 3:
        print("Invalid input")
    elif math[1] not in lst:
        print("Invalid input")
    else:
        x = float(math[0])
        y = float(math[-1])
        if math[1] == "+":
            print(x + y)
        elif math[1] == "-":
            print(x - y)
        elif math[1] == "*":
            print(x * y)
        elif math[1] == "/":
            if y == 0:
                print("Cannot divide by zero")
            else:
                print(x / y)



    
main()