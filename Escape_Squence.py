#comment
""" multiline comment
line2
line 3
"""
#\n: new line
a="abc\npqr"
print(a)

# \r : carriage return
print("abc\rpqr")
print("abc\rpq")
a="abcpqr\rxy"
print(a)

#\b: backspace
print("abc\bpqr")
print("abc12344\bpqr")

#\t tab
print("abc12344\tpqr")

#\v veritcal tab
print("abc12344 \v pqr")

#\0 null
print("abc12344\0pqr")

#\N

#\U :unicode 8 digits
print("abc12344 \U00000100 pqr")

#\u:
print("abc12344 \u0100 pqr")

#prevent Escape sequence
print(r"C:\Users\newFolder")
print("C:\\Users\\newFolder")



