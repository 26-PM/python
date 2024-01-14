# f=open("file.txt","r")
# # f.write("Hello World!")
# content=f.read()
# print(content)
# f.close()

with open("file.txt","r") as f:
    content=f.read()
    print(content)