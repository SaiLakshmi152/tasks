s=input()
l=[]
for i in range(len(s)):
    if(s[i].isnumeric()):
        l.append(s[i])
if(len(l)==0):
    print(-1)
else:
    print(*l,sep=",")
'''You will be given a string, print the list of numbers (from the input string), 

Note: You need to discard special character if any in the input string.



Input:  :a string consists of alpha numeric values

Example 1:

n = 12345

outtut :  1,2,3,4,5'''
