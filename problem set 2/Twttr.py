name = input("Input:").strip()


vowels = ["a", "e", "i", "u", "o"]


lst = []
for char in name:
    if char.lower() not in vowels:
        lst.append(char)

output = "".join(lst)

print(f"output: {output}")
