def main():
    file = input("File name: ")
    print(f"Image/{fileEtenssion(file)}")
        

def fileEtenssion(filename):
    filename = filename.lower().strip()

    if "." in filename:
        return filename.split(".")[-1]
    else:
        return "None"
main()  
