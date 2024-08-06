#using print function
print("%6d"%(100))
print("%4d"%(100))
print("%6.2f"%(23.789))
print("%6.2f"%(0.035))
print("%6.2e"%(956.089666))
print("%4o"%(57))
print("%4.2o"%(57))
print("%4x"%(10))
print("%4s"%("100"))
print("%4.2s"%("10900"))
print("%5.2f"%(2.3789))
print("%-5.2f"%(2.3789))
print("%+5.2f"%(2.3789))
print("%+5.2f"%(-2.3789))
print("viewer%05d M,Subscriber %8.2f M" % (453,9.058))

#using format function
print("my name is {1} & i'm good {0}".format("abc","pqr"))
print("my name is {v2} & i'm good {v1}".format(v2="abc",v1="pqr"))
print("my name is {1:010,.3f} & i'm good {0:,}".format(1235456,5689))

#other methods
print("abc".center(20))
print("abc".center(20,'*'))
print("abc".ljust(20,'*'))
print("abc".rjust(20,'*'))
print("abc".zfill(20))

#other method
a="abc"
print(f'my name is {a}')