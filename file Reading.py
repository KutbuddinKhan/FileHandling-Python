f = open("harry.txt",'rt')
print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())
#
# content = f.read()
#
# for line in f:
#     print(line,end="")
#
# print(content)
# content = f.read(300)
# print("1 ",content)
#
# content = f.read(4)
# print("2 ",content)
f.close()