
def main():
    text = input("Enter Text: ")
    print(makeFaces(text))


def makeFaces(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()