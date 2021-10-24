from math import sqrt
def prime(m):
    if(m==1):
        return 0
    for i in range(2,int(sqrt(m))+1):
        if(m%i==0):
            return 0
    return 1

n=input()
esum=0
osum=0
psum=0
for i in range(len(n)):
    if(n[i].isnumeric()):
        m=int(n[i])
        if(prime(m)):
            psum+=m
        if(m%2==0):
            esum+=m
        else:
            osum+=m
if(esum==0 and psum==0 and osum==0):
    print("-1")
else:
    if(esum==0):
        print("-1",end=" ")
    else:
        print(esum,end=" ")
    if(osum==0):
        print("-1",end=" ")
    else:
        print(osum,end=" ")
    if(psum==0):
        print("-1",end=" ")
    else:
        print(psum,end=" ")
'''You will be given a number, 

print the even digits sum, odd digits sum, and prime number sum

Note:

 You need display the output delimited (separated by) white space.
  if any sum is missed, print -1 as output, for example :
if there is no even numbers sum : -1 
if there is no odd numbers sum : -1
if there is no prime numbers sum : -1
Input:  :a number (n)

Example 1:

n = 1234567

Output:  12 16, 17'''
