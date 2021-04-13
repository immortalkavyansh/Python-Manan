"""
open
read
read line
"""
# f = open("harry.txt", "rt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
# f.close()

"""
writing
appending
"""
# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
# f = open("harry2.txt", "r+")
# print(f.read())
# f.write("thank you")
#
"""
tell
seek
"""
# f = open("harry.txt")
# f.seek(11)
# print(f.tell())
# print(f.readline())
# # print(f.tell())
#
# print(f.readline())
# # print(f.tell())
# f.close()
"""
With block
"""
# with open("harry.txt") as f:
#     a = f.readlines()
#     print(a)

# f = open("harry.txt", "rt")
# Question of the day - Yes or No and why?
# f.close()


