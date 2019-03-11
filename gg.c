#include<stdio.h>
int main()
{
int m,l,di,s=0,t,q;
scanf("%d%d%d",&n,&l,&di);
for(q=0;q<m;q++)
{
t=s+l;
s=t;
l=l+di;
}
printf("%d",t);
return 0;
}
