#include<stdio.h>
#include<stdlib.h>
using namespace std;
struct tree
{

   int data;
   struct tree *right;
   struct tree *left;


}typedef tree;

int pre[100];
int in[100];
int inn=0;
void displayInorder(tree* root)
{
    if(root==NULL)
     return;
    displayInorder(root->left);
    printf("%d ",root->data);
    displayInorder(root->right);
}
tree* create(int data)
{
    tree *x;
    x=(tree *)malloc(sizeof(tree));
    x->data=data;
    x->left=NULL;
    x->right=NULL;
    return x;
}
int foo(int l,int h,int key)
{
    int i;
    for(i=l;i<=h;i++)
    {
        if(in[i]==key)
            return i;
    }
}
tree* build(int start,int end)
{
    if(start>end)
        return NULL;

    tree *temp= create(pre[inn]);
    inn++;

    if(start==end)
        return temp;
    int index=foo(start,end,temp->data);


    temp->left=build(start,index-1);
    temp->right=build(index+1,end);



}
int main()
{
    int i,n;
    printf("Enter no of nodes\n");
    scanf("%d",&n);
    printf("enter inorder traversal\n");
    for(i=0;i<n;i++)
    {
      scanf("%d",&in[i]);
    }
     printf("enter preorder traversal\n");
    for(i=0;i<n;i++)
    {
      scanf("%d",&pre[i]);
    }
    tree* root;
    root= build(0,n-1);
    displayInorder(root);
    return 0;
}
