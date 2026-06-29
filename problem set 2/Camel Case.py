name = input("Camel Case:")

# check at first if name is lower or not

if name.islower():
    print(name)
    exit()

res = ""

for i, letter in enumerate(name):
    if name[i].isupper():
        if name[i] == 0:
           res += name[i].lower()
        else:
            res += name[i].lower() + "_"
    else:
        res += letter

print(res)



"""
# convert the string into a dictionary
dic = {}
for index in range(len(name)):
    dic[index] = name[index]


for i in dic:
    # check if the letter is upper case or no
    if dic[i].isupper():
        if i == 0:
            dic[i] = dic[i].lower()
        # convert the upper case letter into lower case
        else:
            dic[i] = dic[i].lower()
        # add _ for the string to match the snake case
            dic[i] = "_" + dic[i]

# return the dic into string again

snake  = "".join(dic.values())

print(snake)

"""
