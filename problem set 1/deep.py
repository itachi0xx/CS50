def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    answer = answer.strip().lower()    

    if answer == "42" or "forty-two" or "forty two":
        print("YES")
    else:
        print("NO")


main()              
