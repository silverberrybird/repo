# l=[1,2,2,23,3,4,4,4]
# print(l)
# l1=[-1,-2,0,1,2,3,4,5,6]
# l2=[1.3,4.3,2.2]
# l3=['a','b','c']
# l4=[1+2j,2+3j]
# l5=[1,3.4,'s']
# el=[]
# print(el)
# print(type(el))
#
# ll=[10,2,3,4,5,6,
#     7,8,9,76,434,32,
#     54,66,77
#     ]
# print(ll)
# nl=[[1,22,4,65],[5,4,6,7,3]]
# print(nl)
# a="python"
# print(list(a))
# l=[1000]
# print(l)
# print(list(l))
# a=[]
# # print(a and 0)
# # print(0 and a)
# # print(1 and a)
# # print(a and 1)
# # print(2 and a)
# print(0 or a)
# print(1 or a)
# print(a or 1)
# print(a or 0)
# print(2 or a)

# Accessing a list
# l=[1,2,3,4,5,6,7,8,9,0]
# print(l[7])
# print(l[-7])
# print(l[10])
# print(l[-10])

# l=[1,2,3,4,5,[56,67]]
# print(l[5])
# print(l[5][0])
# print(l[-1][1])
# print(l[-1][-2])


#Traversing a list
# l=[1,2,3,4,5,6,7,8,9]
# # for i in l:
# #     print(i)
# #
# # for i in range(len(l)):
# #     print(l[i])
# # i = 0
# # while i < len(l):
# #     print(l[i])
# #     i += 1
#
# # for i,j in enumerate(l,800):
# #     print(i,j)
#
# l1=[i**2 for i in l]
# print(l)
# print(l1)

#slicing
# list1 = [10,20,30,40,50,60,70,80,90,100]
# print(list1)
# print(list1[0:5])
# print(list1[:5])
# print(list1[5:])
# print(list1[:])
# print(list1[-5:-2])
# print(list1[-2:-5])
# print(list1[:11])
# print(list1[3:0])
# print(list1[4:None])
# print(list1[-4:9])
# print(list1[-9:])
# print(list1[::2])
# print(list1[1::2])
# print(list1[::-1])
# print(list1[-5:-2:1])
# print(list1[-2::2])

# # list is mutable
# j=1
# print(id(j))
# j=2
# print(id(j))
# j=1
# print(id(j))
# j="abc"
# print(id(j))
# j[0]="p"

l=[1,2,3,4,5,6,6,7]
print(l)

# using indices
# l[5]="wall"
# print(l)
# l[-2]="moon"
# print(l)

# using slicing
# l[3:5]=[10,20]
# print(l)
# l[0:2]=['one','two']
# print(l)
# l[0:2]="ab"
# print(l)
# l[0:2]="12"
# print(l)
# # l[0:2]=12
# # print(l)
# l[0:2]=1,2
# print(l)
# l[0:2]=1.5
# print(l)
# l[0:3]=[100,200]
# print(l)
# l[3:20]=['three','four']
# print(l)
# l[5:2]=['five','six']
# print(l)
# l[-5:-2]="xy"
# print(l)
# l[1:3:-1]="hd"
# print(l)
# l[-6:-3:-1]=[1,2]
# print(l)
# l[-6:-3:1]=[80,90,70]
# print(l)
# l[-3:-6:-1]=[80,90,70]
# print(l)