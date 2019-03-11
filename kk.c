#include<stdio.h>
#include<conio.h>
void main()
{
    int q,mp;
    scanf("%d%d",&n,&mp);
    int a[q],count,i,j,b[mp];
    for(i=0;i<q;i++)
        scanf("%d",&a[i]);
    for(i=0;i<mp;i++)
        scanf("%d",&b[i]);
    for(i=0;i<mp;i++)
    {count=0;
        for(j=0;j<q;j++)
        {
            if(b[i]==a[j])
                count++;

        }
        if(count==0)
            break;
    }
    if(i==mp)
        printf("Yes");
    else
        printf("No");

}
getch();
