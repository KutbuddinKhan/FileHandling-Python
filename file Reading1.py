f = open("kkhan.txt",'rt')
# print(f.readlines())

# content = f.read()
for line in f:
    print(line,end="")

# content = f.read(100)
# print("1",content)
#
# content = f.read(8)
# print("2",content)

# print(f.readline())
# print(f.readline())
# print(f.readline())

# content = f.read()
# print(content)

f.close()