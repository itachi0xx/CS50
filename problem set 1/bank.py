def main():
   
    greet = input("greeting: ") 
    print(bankGreating(greet))

def bankGreating(input):
    input = input.strip().split()
    if input[0].lower() == "hello":
        return "$0"
    elif input[0][0] == "h" or input[0][0] == "H":
        return "$20"
    else:
        return "$100"


main()    