#include <stdio.h>
unsigned long long int fctrl(int n)
{
    unsigned long long int l=1;
    for(int i=2; i<=n; i++)
    {
        l*=i;
    }
    return l;
}
void fctrn(int n)
{
     
    unsigned long long int h=n, t=0, s=0;
    while (h>0)
    {
        t=h%10;
        s+=fctrl(t);
        h/=10;
    }
    if (s==n)
    {
        printf("%d is factorion", n);
    }
    else
    {
        printf("%d isn't factorion", n);
    }
}
int main ()
{
    int n;
    unsigned long long int r=0, k;
    do
    {
        printf("enter a positive integer: ");
        scanf("%d", &n);
    }
    while (n<0);
    if (n>20)
    {
        printf("Sorry, but it's impossible to calculate the factorial due to the overflow.\n");
        goto factorion;
    }
    k = fctrl(n);
    while (k>9)
    {
        k/=10;
        r++;
    }
    printf("%llu×10^%llu is the factorial for %d\n",k,r,n);
    
    factorion:
    fctrn(n);
    return 0;
}