#include<stdio.h>
#include<string.h>
#include<ctype.h>
int check_9(char x[],int x_length)
{
int j,p=0;
for(j=0;j<x_length;j++)
{
if(x[j]=='9')
{
p++;
}
}
if(p==x_length)
return 1;
else
return 0;


}
int main()
{
char a[1000002];
int length;
int left,right,just;
char original[1000002];
int test_cases;
scanf("%d\n",&test_cases);
while(test_cases!=0)
{
test_cases--;
gets(a);
length=strlen(a);
left = 0;
right=length-1;
strcpy(original,a);
int p2,p1,i;
if(length==1)
{
if(a[0]=='9')
printf("11\n");
else
{
a[0]++;
printf("%c\n",a[0]);
}
}
else if(check_9(a,length)==1)
{
int k;
printf("1");
for(k=0;k<length-1;k++)
printf("0");
printf("1\n");
}
else if(length%2!=0)
{ int mid=(length-1)/2;
while(left<=right)
{ a[right]=a[left];
if(left==right)
{
if(strcmp(original,a)>=0)
{ if(a[mid]!='9')
a[mid]++;
else
{
a[mid]='0';
for(p1=mid-1,p2=mid+1;p1>=0,p2<=length;p2++,p1--)
{
if(a[p1]!='9')
{
a[p1]++;
a[p2]=a[p1];
break;
}
else
{
a[p1]='0';
a[p2]=a[p1];
}
}
}
}
}
left++;right--;
}
for(i=0;i<length;i++)
printf("%c",a[i]);
printf("\n");
}
else if(length%2==0)
{
while(left<=right+1){
a[right]=a[left];
if(right-left==1)
{
if(strcmp(original,a)>=0)
{
if(a[left]!='9')
{
a[left]++;
a[right]=a[left];
}
else{
for(p1=left,p2=right;p1>=0,p2<=length;p1--,p2++)
{
if(a[p1]!='9')
{
a[p1]++;
a[p2]=a[p1];
break;
}
else
{
a[p1]='0';
a[p2]=a[p1];
}
}
}
}
}
left++;
right--;
}
for(i=0;i<length;i++)
printf("%c",a[i]);
printf("\n");
}

}

return 0;
}
