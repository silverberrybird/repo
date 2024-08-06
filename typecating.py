# #type of data
# print(type(10))

#convert to int
a = 10.3
print(type(a))
b = int(a)
print(type(b))
b = '110'
print(type(b))
print(int(b , 2))
C = 'f'
print(type(C))
print(int(C, 16))
d = '0o17'
print(int(d , 8))
print(int(1.235e3))

#convert to float
a = '10'
print(type(a))
print(float(a))
print(float(20))

#convert to string
a = 10
print(type(a))
print(str(a))
print(str(10.4))
a = 20
b = hex(a)
print(b)
print(type(b))
a = 20
b = oct(a)
print(b)
print(type(b))
a = 20
b = bin(a)
print(b)
print(type(b))
a = 2+4j
print(str(a))

#character to decimal
a = 'A'
print("decimal value of character is :", ord(a))

#Decimal to character
a = 65
print("character value of decimal is :", chr(a))

