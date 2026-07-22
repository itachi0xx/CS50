def main():

    user_input = input("Input: ")

    print(shorten(user_input))



def shorten(word):

    vowels = ["i", "o", "u", "e", "a"]

    lst = []

    for char in word:
        if char.lower() not in vowels:
            lst.append(char)

    output = "".join(lst)

    return output

if __name__ == "__main__":
    main()
