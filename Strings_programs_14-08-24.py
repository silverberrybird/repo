# WAPPT calculate length of string
# s = "Who is Rushabh Patwa?"
# c = 0
# for i in s:
#     c += 1
# print(c)

# WAPPT check whether given string is palindrome or not
# a = input('Enter a string: ')
# b = a[::-1]
# if a==b:
#     print('The string is a palindrome')
# else:
#     print('The string is not a palindrome')

# WAPPT Get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# a = input('Enter a string: ')
# c = 0
# for i in a:
#     c += 1
# if c <= 2:
#     print()
# else:
#     print(a[:2]+a[-2:])

# WAPPT add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# a = input('Enter a string: ')
# c = 0
# for i in a:
#     c += 1
# if c <= 2:
#     print()
# else:
#     if a[-3:] == 'ing':
#         print(a+'ly')
#     else: print(a+'ing')

# WAPPT get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.
# a = input('Enter a string: ')
# b = a[0]
# c = a.replace(b,'$')
# print(b+c[1:])

# WAPPT get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# a = input('Enter a string: ')
# b = input('Enter another string: ')
# c = (b[:2] + a[2:] + ' ' + a[:2] + b[2:])
# print(c)

# WAPPT remove nth index character from a non empty string
# a = input('Enter a string: ')
# b = int(input('Enter index to be removed: '))
# print(a[:(b-1)] + a[b:])

# WAPPT remove characters that have odd index values in a given string.
# a = input('Enter a string: ')
# c = ""
# for i in range(len(a)):
#     if i % 2 == 0:
#         c += a[i]
# print(c)

# WAPPT convert given string to all uppercase if it contains atleast two uppercase characters in first four characters
# a = input("Enter a string: ")
# c = 0
# for i in a[:4]:
#     if i.upper() == i:
#         c += 1
# if c >= 2:
#     print(a.upper())
# else:
#     print("Does not contain min two uppercase char in first four char")

# WAPPT remove a new line in python
# a = """Enter a string:
# sdlslgnlkn
# gnskgn\n\n\n\n"""
# print(a.rstrip('\n'))

# WAPPT count the occurence of a substring in a given string
# a = input('Enter a string: ')
# b = input('Enter a substring: ')
# print(b, "occurs", a.count(b), "times in", a)

