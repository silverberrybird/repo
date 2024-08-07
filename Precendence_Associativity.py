# Precedence of operators
# (), **, ~, *, /. %, //, +, -, <<, >>, &, ^, |, >, <, ==, !=,
# in, not in, is, is not, >=, <=, not, and, or, assignment operators

print(110-3*2)
print((110-3)*2)
print((10-3)**2)
print(10-3**3)
a,b="abc",0
print(a=='abc'and a=="abcd" or b>2)
print(a=="abc"and a=="abcd" or b=="abcd")
print(10&8|8^10)

# Associativity of operators
# right to left **, unary operators, not, assignment operators
# rest left to right

