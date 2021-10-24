'''you are given JNTUK roll number of a B.Tech., student of any branch 15P31A0523 in which first two characters represent admitted year of a student and 5th and 6th characters collectively defines nature of admission either regular if it is 1A or Lateral entry in upper case only if it is 5A your task is to print admitted year in YYYY format and nature of admission separated by space 
Input:
 15P31A0523
output;
2015 REGULAR
Input:
 15P35A0523
output;
2015 LATERAL ENTRY'''
m=input()
if(m[4]=='1'):
    print("20"+(m[0:2]),'REGULAR')
else:
    print("20"+(m[0:2]),'LATERAL ENTRY')
