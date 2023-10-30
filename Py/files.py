#document- https://docs.python.org/3/library/functions.html#open

# file = open("poem.txt")
# print(file.read())
# file.close()

# with open("poem.txt") as file:
#     for line in file:
#         text = line.upper()
#         print(text.strip())

# with open("writefile.txt", "w") as file: #write
#     file.write("The blood of the covenant is thicker than the water of the womb.")

# with open("writefile.txt", "a") as file: #append
#     file.write("Chosen bonds are more significant than the bonds with family or “water of the womb.” More directly, it means that relationships you make yourself are far more important than the ones that you don't choose.")


with open("writefile.txt") as file:
    text = file.readline()
    print(text.upper().strip())
    print(file.read())