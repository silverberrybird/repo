# a="Python Programing"
# # print(a)
# # print(type(a))
# # a='Python Programing'
# # print(a)
# # print(type(a))
# # a="""A python Programing
# # python is a programming language
# # python is a programming language
# #
# """

#slicing
# print(a)
# # print(a[0])
# # print(a[-1])
# # print(a[-2])
# print(a[2:5])
# print(a[2:])
# print(a[:2])
# print(a[:])
# print(a[-5:-1])
# print(a[2:-5])
# print(a[2::2])
# print(a[::2])
# print(a[::-1])
# print(a[::])

#comparison of string
# a = "Python"
# b = "python"
#
# print("a==b", a==b)
# print("a!=b", a!=b)
# print("a>b", a>b)
# print("a<b", a<b)
# print("a>=b", a>=b)
# print("a<=b", a<=b)

#
# a = "Python@123"
# b = "Python@12345"
#
# print("a==b", a==b)
# print("a!=b", a!=b)
# print("a>b", a>b)
# print("a<b", a<b)
# print("a>=b", a>=b)
# print("a<=b", a<=b)


# #traversing of string
# a="hello world"
# for i in a:
#     print(i,end="")

#inbuilt method of strings
# a="hElLo WoRlD"
# print(a*3)
# b="hi "+a
# print(b)
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())
# print(a.casefold())
# b=a.center(50,"\u1115")
# print(b)
# print(b.count("ᄕ",2,8))
# print(b.endswith("ᄕ",36,48))
# print("Ståle".encode(encoding="ascii",errors="replace"))
# print(b.encode(encoding="ascii",errors="replace"))
# print(b.encode(encoding="ascii",errors="backslashreplace"))
#
# a= "H\te\tl\tl\to"
# print(a)
# print(a.expandtabs())
# print(a.expandtabs(2))
# print(a.expandtabs(4))
# print(a.expandtabs(10))

# a="h e l l o À 'ß' w o r l d "
# # print(a.find("e"))
# print(a.count("l"))
# print(a.find("l",2,4))
# print(a.rfind("l"))
# print(a.rfind("l",2,4))

# print(a.lower())
# print(a.casefold())
# print("12345a".isalnum())
# print(a.isalpha())
# print(a.isdecimal())
# print(a.isdigit())
# print(a.isidentifier())
# print(a.islower())
# print(a.isupper())
# print(a.istitle())
# print(a.isspace())
# print(a.replace("l ", "'ß'_"))
# print(a.replace("l ", "00",1))
# print(a.replace(" ", "'",1))
# print(a.split("'ß'"))
# print(a.split("l"))
# print(a.split("l",2))
# print(a.partition("l"))
# print("abc@gmail@.com".partition("@"))
# print("abc@gmail@.com".rpartition("@")

print("Shital".rjust(20))
print("Shital".rjust(20,'*'))
print("Shital".ljust(20))
print("Shital".ljust(20,'*'))
print("      Shital       ")
print("           Shital       ".strip())
print("ShiStalS".strip('S'))
print("    ShiStalS".lstrip())
print("ShiStalS".lstrip("S"))
print("ShiStalS      ".rstrip())
print("ShiStalS".rstrip("S"))
print("_python_".join("Shital"))
print("python".zfill(20))
a="python"
b=str.maketrans('y','@')
print(b)
print(a.translate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.translate(b))
print(a.isprintable())
