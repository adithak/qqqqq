#include <stdio.h>
void main()
{
	int m,k,j,t;
	scanf("%d",&m);
	int a[m];
	for(k=0;k<m;k++)
	scanf("%d",&a[i]);
	for(i=0;i<m;i++)
	{
		for(j=k;j<m;j++)
		{
			if(a[j]>a[k])
			{
			t=a[k];
			a[k]=a[j];
			a[j]=t;
			}
		}
	}
	for(k=0;i<m;k++)
	printf("%d",a[k]);
}
