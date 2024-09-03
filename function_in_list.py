# l="abcsdcasd"
# print(l)
# print(max(l))
# print(min(l))
# print(min(2 , 3))
# print(sorted(l))
# print(sorted(l,reverse=True))


# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)
# print(type(l))
# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))
# print(sum(l,100))
#
# s=['a','b','c','d','e','f','g','h','i','j']
# print(s)
# # print(sum(s))
# print(max(s))
# print(min(s))
#
# c=[2+2j,4+5j,5+6j,6+6j,7+7j,9+1j]
# print(sum(c))
# print(max(c))
# print(min(c))
# l=[100,455,600,67,900]
# print(l)
# a=sorted(l)
# print(a)
# print(l)
# l=['aaa','av','cda','abcd','aad']
# print(l)
# a=sorted(l)
# print(sorted(l))
# print(sorted(l,reverse=True))
# print(sorted(a,key=len))
# l=[[1,2],[3,4],[1,2,1],[1,3],[1,2,2]]
# print(l)
# print(sorted(l))
# print(sorted(l,reverse=True,key=len))

# list function
# index function
# l=[10,20,3,2,4,5]
# print(l.index(3))
# print(l.index("3"))
# print(l.index(8))
#
# l=[0,1,True,False]
# print(l.index(True))
# print(l.index(False))
#
# l=[2,1,3,2,-1]
# print(l.index(2))
# print(l.index(2,1))
# print(l.index(2,1,3))
#
# l = [[1, 2], [3, 4], [1, 2, 1], [1, 3], [1, 2, 2]]
# print(l.index([1,2,1]))
#
# l=[{1,2,1},{1,2,1,1},{2,1,1}]
# print(l.index({1,2,1}))
# print(l.index({1,2,1,1}))
# print(l.index({2,1,1}))

# append function
# l=[1,2,3,4,5]
# print(l.append(6))
# print(l)
# print(l.append(7,78))
# l.append([10,20,30,40,50])
# print(l)
# l.append("abc")
# print(l)
# l.append(1+2j)
# print(l)

# extend function
# l="abc"
# l1=[1,2,3,4,5]
# l1.extend(l)
# print(l1)
# # l1.extend(10)
# print(l1)
# l1.extend(['a','b','c'])
# print(l1)

# insert function
# l=[1,2,3,4,5]
# l.insert(1,"abc")
# print(l)
# l.insert(-2,10)
# print(l)
# l.insert(-1,20)
# print(l)
# l.insert(0,30)
# print(l)
# l.insert(4,40)
# print(l)
# l.insert(-5,50)
# print(l)
# l.insert(6,60)
# print(l)
# l.insert(6,[70,80,90])
# print(l)

# reverse function
# l=[10,20,3,2,4,5]
# l.reverse()
# print(l)
# print(reversed(l))
# a=reversed(l)
# for i in a:
#     print(i)

# sort function
# l=[1,5,6,2,3,4,8,7]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l=['aa','abc','aab','ab','abcd']
# l.sort(key=len)
# print(l)

# count function
# l=[1,2,1,3,4,1,5,6,3]
# print(l.count(1))
# print(l.count(2))
# print(l.count(7))

# pop function
# l=[10,20,3,2,4,5]
# print(l.pop())
# print(l)
# print(l.pop(2))
# print(l)
# print(l.pop(8))
# print(l.pop(2,3))
# print(l.pop([2:]))

# remove function
# l=[10,20,30,40,50]
# l.remove(20)
# print(l)
# print(l.remove(30))
# l.remove(300)
# print(l)

# clear function
# l=[10,20,3,2,4,5]
# l.clear()
# print(l)

# del keyword
# a=10
# print(a)
# del a
# print(a)
#
l=[10,20,3,2,4,5]
del l[1]
print(l)
del l[1:3]
print(l)
del l
print(l)
