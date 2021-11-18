#include<stdio.h>
#include<stdlib.h>
using namespace std;
typedef struct linkedlist
{
 struct linkedlist *next;
 int data;
}List;
void Insert(List **head ,List **current, int data)
{   //current and head are double pointers
    List* temp;
    if(*head==NULL)
    {  *head = (List*)malloc(sizeof(List));
       if(*head==NULL)
        printf("hell!\n");
      (*head)->data=data;
      (*head)->next=NULL;
       *current = *head;
       printf("Head NULL case");

    }
    else
    {    (*current)->next=(List*)malloc(sizeof(List));
         (*current)->next->data=data;
         (*current)=(*current)->next;
         (*current)->next=NULL;
         printf("Head not NUll case");
    }

}
void printlist(List *head)
{
  List* temp;
  if(head==NULL)
    printf("Empty List\n");

  else
  {   temp=head;
      while(temp!=NULL)
      {
          printf("%d->",temp->data);
          temp=temp->next;


      }

  }
}
int main()
{
int choice;
int data;
List *head=NULL;
List *current=NULL;
do
{
    printf("Enter your choice\n");
    printf("1)Insert in the list\n");
    printf("2)Display the list\n");
    scanf("%d",&choice);
    switch(choice)
    {
        case 1:{
            printf("Insert commences\n");
            printf("Enter the number\n");
            scanf("%d",&data);
            Insert(&head, &current , data);
            printf("Head:data %d Current:data %d\n",head->data,current->data);
            break;

        }
        case 2:
            {
                printlist(head);
                break;
            }
        default:{
        printf("Invalid input\n");
        }
    }
}while(choice<3);
return 0;
}
