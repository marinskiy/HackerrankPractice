import numpy 
n,m = map(int,input().split())
l=[]
for i in range(n):
    l1 = input().split(' ')
    l = l+l1
a = numpy.array(l,dtype = numpy.int32)
print(numpy.transpose(a.reshape(n,m)))
print(a)
