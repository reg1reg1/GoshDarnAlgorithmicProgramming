#include<stdio.h>
#include<stdlib.h>
using namespace std;
int level;

int max(int x,int y)
{
    if(x>y)
    return x;
    return y;
}
typedef struct treeNode
{
        int data;
        struct treeNode *left;
        struct treeNode *right;

}treeNode;

treeNode* prev=NULL;
treeNode* head=NULL;
void dbly(treeNode *root)
{
    if(root==NULL)
    return;
    dbly(root->left);
   // printf("e1\n");
    if(prev==NULL)
    {
        prev=root;
        head=root;
       //  printf("e2\n");
    }

    else
    {
        prev->right=root;
      //  printf("e5\n");
        prev=prev->right;

    }
    //// printf("e3\n");
    dbly(root->right);
    //printf("e4\n");
}
void dbly2(treeNode *x)
{
   while(x->right)
   {
       x->right->left=x;
       x=x->right;
   }

}
void display2(treeNode *x)
{

    while(x)
    {
        printf("%d--->",x->data);
        x=x->right;
    }
printf("\n");
}
int depthoftree(treeNode *x)
{
    if(x==NULL)
    return 0;
    else return max(depthoftree(x->left),depthoftree(x->right))+1;
}
void printG(treeNode *root,int level,bool ltr)
{
       if(root==NULL)
        return;
       if(level==1)
       printf("%d ",root->data);

       else if(level>1)
       {
           if(ltr)
           {
               printG(root->left,level-1,ltr);
               printG(root->right,level-1,ltr);
                //printf("\n");
           }

           else
           {
               printG(root->right,level-1,ltr);
               printG(root->left,level-1,ltr);
              // printf("\n");
           }
       }


}
void printspiral(treeNode *root)
{
    int h=(depthoftree(root));
    int i;
    bool ltr=false;
    for(i=h;i>=0;i--)
    {
        printG(root,i,ltr);
        ltr=!ltr;
    }

}

void mirror(treeNode *x)
{
    if(x==NULL)
    return;
    else
    {
        treeNode *temp;
        mirror(x->left);
        mirror(x->right);

        temp=x->right;
        x->right=x->left;
        x->left=temp;
    }



}

treeNode* FindMin(treeNode *node)
{
        if(node==NULL)
        {

                return NULL;
        }
        if(node->left)
                return FindMin(node->left);
        else
                return node;
}
treeNode* FindMax(treeNode *node)
{
        if(node==NULL)
        {

                return NULL;
        }
        if(node->right)
                FindMax(node->right);
        else
                return node;
}

treeNode * Insert(treeNode *node,int data)
{
        if(node==NULL)
        {
                treeNode *temp;
                temp = (treeNode *)malloc(sizeof(treeNode));
                temp -> data = data;
                temp -> left = temp -> right = NULL;
                return temp;
        }

        if(data >(node->data))
        {
                node->right = Insert(node->right,data);
        }
        else if(data < (node->data))
        {
                node->left = Insert(node->left,data);
        }
        else
        {
            printf("Data already exists\n");
        }
        return node;

}

treeNode * Delete(treeNode *node, int data)
{
        treeNode *temp;
        if(node==NULL)
        {
                printf("Element Not Found");
        }
        else if(data < node->data)
        {
                node->left = Delete(node->left, data);
        }
        else if(data > node->data)
        {
                node->right = Delete(node->right, data);
        }
        else
        {

                if(node->right && node->left)
                {

                        temp = FindMin(node->right);
                        node -> data = temp->data;

                        node -> right = Delete(node->right,temp->data);
                }
                else
                {

                        temp = node;
                        if(node->left == NULL)
                                node = node->right;
                        else if(node->right == NULL)
                                node = node->left;
                        free(temp);
                }
        }
        return node;

}

void Find(treeNode *node, int data)
{
        if(node==NULL)
        {

                printf("Data Non existent\n");
        }
        if(data > node->data)
        {

                level++;
                Find(node->right,data);
        }
        else if(data < node->data)
        {
                level++;
                Find(node->left,data);
        }
         else
         {
             printf("Found at level %d\n",level);
         }
}

void PrintInorder(treeNode *node)
{
        if(node==NULL)
        {
                return;
        }
        PrintInorder(node->left);
        printf("%d ",node->data);
        PrintInorder(node->right);
}

void PrintPreorder(treeNode *node)
{
        if(node==NULL)
        {
                return;
        }
        printf("%d ",node->data);
        PrintPreorder(node->left);
        PrintPreorder(node->right);
}

void PrintPostorder(treeNode *node)
{
        if(node==NULL)
        {
                return;
        }
        PrintPostorder(node->left);
        PrintPostorder(node->right);
        printf("%d ",node->data);
}

int main()
{
        treeNode *root = NULL;
        treeNode *thead;
        int choice,data;
        do{
        printf("Welcome to binary search tree\n");
        printf("1)Insert into tree\n");
        printf("2)Delete from tree\n");
        printf("3)Display tree \n");
        printf("4)Search in tree\n");
        printf("5)Print depth of tree\n");
         printf("6)Convert to mirror of tree\n");
         printf("7)Conevert to DLL\n");
        scanf("%d",&choice);
        if(choice==1)
        {
            printf("Enter your data\n");
            scanf("%d",&data);
           root=Insert(root,data);

           thead=root;

        }
        if(choice==2)
        {
            printf("Enter the data to be deleted\n");
            scanf("%d",&data);
            root=Delete(root,data);


        }
        if(choice==3)
          {  int order;
             printf("Which way?\n");
             printf("1)Inorder\n");
             printf("2)Preorder\n");
             printf("3)Postorder\n");
             printf("4)Levelorder in spiral form\n");
             scanf("%d",&order);
             if(order==1)
             {
                 PrintInorder(root);
                 printf("\n\n");
             }
            if(order==2)
             {
                 PrintPreorder(root);
                 printf("\n\n");
             }
             if(order==3)
             {
                 PrintPostorder(root);
                 printf("\n\n");
             }
             if(order==4)
             {

                 printspiral(root);
                 printf("\n\n");
             }
          }
          if(choice==4)
          {
             // level=0;
              printf("Enter data to be searched\n");
              scanf("%d",&data);
              //treeNode *temp1;
              Find(root,data);

          }
          if(choice==5)
          {
              printf("Depth %d\n",depthoftree(root));
          }
          if(choice==6)
          {
              mirror(root);
          }
          if(choice==7)
          {

              //printf("%d",root->left->data);
              dbly(thead);

             // printf("x");
              dbly2(head);
              //printf("y");
              treeNode *head2;
              head2=head;
              display2(head2);
          }
}while(choice<8);
return 0;
}
