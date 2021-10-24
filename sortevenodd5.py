l=list(map(int,input().split(',')))
m=[]
n=[]
o=[]
for i in range(len(l)):
    if(l[i]%2==0):
        m.append(l[i])
        m.sort()

for i in range(len(l)):
    if(l[i]%2!=0):
        n.append(l[i])
        n.sort()
#print(m)
#print(n)
o=m+n
#o.append(m)
#o.append(n)
print(o)
'''Given an array of integers, sort the array in the given sequence, that is, first EVEN numbers, then followed by the ODD numbers of the given array of elements.

Example1

Given input array is  = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]

 Output  Expecting is =  [ 2, 4, 6, 8, 10, 12, 3, 5, 7, 9, 11]'''
