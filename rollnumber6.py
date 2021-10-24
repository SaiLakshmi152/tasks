n=input()
if(n.isalpha() or n.isnumeric()):
    print(-1)
else:
    print("Year of Admission:",n[0:2])
    print("College Code:",n[2:4])
    print("Branch Code:",n[4:6])
    print("Program Code:",n[6:8])
    print("Student Number:",n[8:10])

    
'''You will be given a string (STUDENT REGISTRATION NUMBER, it is an Alphanumeric)

Extract the following information and print the same in the same order

Year of Admission Number, 
College Code
Branch Code
Program Code
Student Number
Input:  : JNTUK Student Registration Number

Output:  Year of Admission, College Code, Program Code, Branch Code'''
