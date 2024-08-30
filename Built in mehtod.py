#id() function
# print(id("Hello World"))
# a=10
# print(id(a))
# b=a
# print(id(b))
# b=10
# print(id(b))
# print(id(a+b))

# a="hello world"
# b="python"
# print(id(a))
# print(id(b))
# print(id(a+b))

# a="okk"
# for i in a:
#     print(id(i))

# a=10
# print(id(a))
# a=20
# print(id(a))
# print(id(a*3))
#
# a="python"
# print(id(a))
# print(id(a[:]))
# print(id(a[2:]))
# print(id(a[:2]))
# print(id(a[1:5]))
# print(id(a[5:2:-1]))

# enumerate function
# a="okk"
# for i in a:
#     print(i)

# a="hello world"
# for i in range(len(a)):
#     print(i,"=",a[i])
#
a = "hello world"
print(type(a))
print(enumerate(a))
b = enumerate(a)
print(type(b))
# for i in enumerate(a):
#     print(i)

# for i,j in enumerate(a):
#     print(i,j)

for i in enumerate(a,947):
    print(i)