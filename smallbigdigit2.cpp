/*In a NUMBER, All you need to do is find the Smallest Digit and Biggest digit in the given Five Digit Number.

Input:

The input contains Five Digit Number (n)

Constraint(s):

10000 <=  n <=99999

Example 1:

n = 52134

Smallest =1

Biggest = 5*/
#include<stdio.h>
int main()
{
    int num,small,big,rem;
    small=9;
    big=0;
    printf("enter a number");
    scanf("%d",&num);
    while(num>0)
    {
        rem=num%10;
        if(rem<small)
        {
            small=rem;
        }
        if(big<rem)
        {
            big=rem;
        }
        
        num=num/10;
    }
    printf("%d\n",small);
    printf("%d\n",big);
    return 0;
}
