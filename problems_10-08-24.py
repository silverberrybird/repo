# WAPPT check whether a given number is prime or not
# a = int(input("Enter a number: "))
# if a == 1:
#     print("Number is neither prime nor composite")
# i = 2
# while i <= a:
#     if a == 2:
#         print("Number is prime")
#     elif a % i == 0:
#         print("Number is not prime")
#         break
#     else:
#         print("Number is prime")
#         break
#     i += 1

# WAPPT find those numbers which are divisible by 7 and multiples of 5 between 1500 and 2700
# a = 1500
# while a <= 2700:
#     if a % 7 == 0 and a % 5 == 0:
#         print(a,"is divisible by 7 and 5")
#     a += 1

# WAPPT get Fibonacci series upto 50
# a = 1
# sum = 0
# while sum < 50:
#     print(sum)
#     sum = sum + a
#     a = sum - a

# WAPPT print star pattern
# i =1
#
# while i < 4:
#     j = 0
#     while j<i :
#         print('*',end="")
#         j += 1
#     print()
#     i = i + 1

# WAPPT uppar vala shirko ulto triangle
# i = 1
# while i <= 4:
#     j = 4
#     while j >= i:
#         print('*',end="")
#         j -= 1
#     print()
#     i += 1

# WAPPT star pattern type 3
# i = 0
# k = 0
# for i in range(4):
#     for k in range(3-i):
#             print(" ",end="")
#             k += 1
#
#     for j in range(0,i+1):
#         print("*",end="")
#         j -= 1
#     print()
#     i += 1

# WAPPT star pattern type 4
# i = 0
# k = 0
# for i in range(4):
#     for k in range(i):
#         print(" ",end="")
#         k -= 1
#     for j in range(4-i):
#         print("*",end="")
#         j += 1
#     print()
#     i += 1

# WAPPT proper pyramid 1
# for i in range(4):
#     for k in range(3-i):
#         print(" ",end="\t")
#         k += 1
#     for j in range(2*i+1):
#         print("*",end="\t")
#         j += 1
#     print()
#     i += 1

# WAPPT proper pyramid uppar shirko pan ulto
# for i in range(4,0,-1):
#     for k in range(4-i):
#         print(" ",end="\t")
#     for j in range(2*i-1):
#         print("*",end="\t")
#     print()

# WAPPT 1 2 3 walo pyramid
# for i in range(4):
#     for k in range(3-i):
#         print("  ",end="\t")
#         k += 1
#     for j in range(i+1):
#         print("*",end="   ")
#     print()

# # to display stars in equilateral triangular form
# n=4
# for i in range(1, 5):
#     print(' '*n, end='') # repet space for n times
#     print('* '*(i)) # repeat stars for i times
#     n-=1

# WAPPT print following pattern (output me dekh leije)
# i =1
# c = 0
# while i < 8:
#     j = 0
#     while j<i :
#         l=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5]
#         if c == 17:
#             c = 1
#         print(l[c],' ',end="")
#         c += 1
#         j += 1
#     print()
#     i = i + 1

# WAPPT print letters triangle pattern
# i =1
# c = 65
# while i < 8:
#     j = 0
#     while j<i :
#         print(chr(c),' ',end="")
#         c += 1
#         if c == 91:
#             c = 65
#         j += 1
#     print()
#     i = i + 1

# WAPPT print A AB ABC triangle pattern
# i =1
# c = 65
# while i < 8:
#     j = 0
#     c = 65
#     while j<i:
#         print(chr(c),' ',end="")
#         c += 1
#         j += 1
#     print()
#     i = i + 1

# WAPPT print sideways triangle star
# n = int(input('Enter a number: '))
# c = 1
# i = 1
# d = 1
# while i <= 2 * n - 1:
#     while c <= n:
#         print('* ', end='')
#         c += 1
#     print()
#     i += 1
# draft 2
# for i in range(4):
#     for k in range(3-i):
#         print(" ",end="\t")
#         k += 1
#     for j in range(2*i+1):
#         print("*",end="\t")
#         j += 1
#     print()
# for i in range(4,0,-1):
#     for k in range(4-i):
#         print(" ",end="\t")
#     for j in range(2*i-2):
#         print("*",end="\t")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="\t\t")
#     print()
# for i in range(5, 0, -1):
#     for j in range(i-2, -1, -1):
#         print("*", end="\t\t")
#     if i != 1:
#         print()

# WAPPT satva alankar number pyramid
# n = int(input('Enter a number: '))
# for i in range(n):
#     for k in range(n - i - 1):
#         print("", end="\t")
#     for j in range(i + 1):
#         print(j + 1, end="\t")
#     for t in range(i, 0, -1):
#         print(t, end="\t")
#     print()

# WAPPT saatvaa (7th) alankar pyramid
# n = 8
# l = ['सा', 'रे', 'ग', 'म', 'प', 'ध', 'नि', 'सा']
# # l = ['do', 're', 'mi', 'fa', 'so', 'la', 'ti', 'do']
# for i in range(n):
#     for k in range(n - i-1):
#         print("", end="\t")
#     for j in range(i + 1):
#         print(l[j], end="\t")
#     for t in range(i,0, -1):
#         print(l[t-1], end="\t")
#     print()
