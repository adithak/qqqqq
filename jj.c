int main()
{
    int q[10],a,d,i,j;
    scanf("%d",&b);
    for(i=0;i<a;i++)
    {
      scanf("%d",&q[i]);  
    }
    for(i=0;i<a;i++)
   { 
       for(j=i+1;j<a;j++)
       {
           d=a[i]+q[j];
       if(d>a[j]&&d<=a[a-1])
       {printf("\n %d %d %d",q[i],q[j],d);
       }}}
    return 0;
}
