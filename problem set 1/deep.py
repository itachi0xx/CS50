
def main():
    ans = input("What is the answer to the Ultimate Question of Life, The Universe, and Everything? ")
    deepThoughts(ans)

def deepThoughts(input):
 input = input.lower().strip()
 if input == "42" or input == "forty-two" or input == "forty two":
  print("Yes!")
 else:
  print("No!")

main()
