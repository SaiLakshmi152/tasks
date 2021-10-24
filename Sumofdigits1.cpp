/*You will be given a FIVE DIGIT NUMBER, All you need to do is find the sum of the digits of the given Five Digit Number.

Input:

The input contains Five Digit Number (n)

Constraint(s):

10000 <=  n <=99999

Example 1:

n = 34245

sum = 3 + 4 + 2 + 4 + 5  = 18*/
#include<stdio.h>
int main()
{
 int num,sum=0,rem,count=0;
 printf("enter a number");
 scanf("%d",&num);
 if(num==0)
 {
     printf("-1");
 }
 else
 {
 while(num)
 {
  rem=num%10;
  sum=sum+rem;
  num=num/10;
  count=count+1;
 }
 if(count==5)
 {
  printf("the sum of digits is %d",sum);
 }
 else
 {
     printf("-1");
 }
 }
 return 0;
}
/*In a NUMBER, All you need to do is find the Smallest Digit and Biggest digit in the given Five Digit Number.

Input:

The input contains Five Digit Number (n)

Constraint(s):

10000 <=  n <=99999

Example 1:

n = 52134

Smallest =1

Biggest = 5*/
