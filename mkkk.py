# f = open("demo.txt", "r")

# data = f.read(5)
# print(data)

# f.close()

# f =open("demo.txt", "r")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()

# f = open("demo.txt", "a")

# f .write("\nafter that i will come")
         
# f.close()

# f = open("simple.txt", "w")
# f.close()

# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()

# with open("demo.txt", "r")as f:
#     data = f.read()
#     print(data)
    
# with open("demo.txt", "w") as f:
#     f.write("new data")    

# import os

# os.remove("simple.txt")

# with open("practice.txt", "w") as f:
#     f.write("this is a simple line\n i am happy")
#     f.write("using java\n i am learning python.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
