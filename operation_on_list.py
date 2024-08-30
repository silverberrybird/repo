# comparing a list
# print([1,2,3,4,5]==[1,2,3,4,5])
# print([1,2,3,4,5]==['a','b','c','d'])
# print([1,2,3,4,5]!=['a','b','c','d'])
# print([1,2,3,4,5]>[1,2,3,4])
# print([1,2,3,8,5]<[1,2,3,6])
# print([1,2,3,4,5]<=[1,2,3,4,5])
# print([1,2,3,4,5,6]>=[1,2,3,4,5])
# # print([1,2,3,4,5]<=['a','b','c','d'])
# print([1,2,3,4,5]==[1.1,2.0,3.0,4.0,5.0])
# print([1,2,3,4,5]==[1.0,2.0,3.0,4.0,5.0])


# concatenation of list
# l=[1,2,3,4,5]
# a=10
# # print(l+a)
# l1=[1,2,3]
# print(l+l1)
# l3=[[1,2,3,4,5]]
# print(l+l3)
# # print(l+"abc")
#
# # +=
# l+=l3
# print(l)
# l+="abc"
# print(l)
# l+=[10,20,30,40,50]
# print(l)

# repatation of list
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l*2)
# # print(l*2.0)
# print(l*-2)
# print(l*2**2)
# print(l*'a')
# l*=3
# print(l)

# Membership operator
# l=[1,2,3,4,5,6,7,8,9]
# print(l)
# print(8 in l)
# print(10 in l)
# print(11 not in l)

# copying of string
# l=[1,2,3,4,5,6,7]
# print(l)
# l1=l
# print(l1)
# l1[0]=5
# print(l1)
# print(l)
# print(id(l))
# print(id(l1))

# 1) list()
# l=[1,2,3,4,5,6,7]
# print(l)
# l1=list(l)
# print(l1)
# l1[0]=5
# print(l1)
# print(l)
# print(id(l))
# print(id(l1))

# 2)copy()
# l=[1,2,3,4,5,6,7]
# print(l)
# l1=l.copy()
# print(l1)
# l1[0]=5
# print(l1)
# print(l)
# print(id(l))
# print(id(l1))

# 3) silicing
l=[1,2,3,4,5,6,7]
print(l)
l1=l[:]
print(l1)
l1[0]=5
print(l1)
print(l)
print(id(l))
print(id(l1))

