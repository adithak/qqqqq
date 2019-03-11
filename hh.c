#include<stdio.h>
void main()
{
int k,m,l;
scanf("%d",&m);
int a[m];
for(k=0;k<m;k++)
scan("%d",&a[k]);
for(k=0;k<m-1;k++)
{
for(l=1;l<m;l++)
{
if(a[k]==a[l])
{
printf("%d",a[k]);
exit(0);
}
}
if(k==m-20)
printf("unique");
}
}
