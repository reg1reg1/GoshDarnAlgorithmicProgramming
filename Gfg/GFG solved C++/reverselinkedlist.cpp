/**
Author : Dark Lord 
Recursive method: Simple tail recursive method
**/

#include <stdio.h>
#include <iostream>
#include <malloc.h>
using namespace std;

struct Node
{
	int data;
	struct Node* next;
};
void Insert(struct Node** headref, int data)
{
	struct Node* node = (struct Node*)malloc(sizeof(struct Node));
   	node->data = data;
   	node->next=NULL;	
   if((*headref)==NULL)
   {
   	
   	(*headref) = node;
   }
   else
   {
    struct Node* curr = (*headref);
    while(curr->next!=NULL)
    {
    	curr=curr->next;
    }
    curr->next= node;
    //free(node);
   }
}
void traverse(struct Node* head)
{
	struct Node* curr = head;
	while(curr!=NULL)
	{
		cout<<curr->data<<" ";
		curr=curr->next;
	}
	cout<<"\n";
}
void reverseIterative(struct Node** headref)
{
	struct Node *temp,*curr,*prev;
	curr=(*headref);
	prev=NULL;
	while(curr!=NULL)
	{
		temp = curr->next;
		curr->next=prev;
		prev= curr;
		curr=temp;
	}
	(*headref)=prev;
}
struct Node* recrev(struct Node* curr, struct Node* prev)
{
	struct Node* temp;
	if(curr==NULL)
	{
		return prev;
	}
	temp=curr->next;
	curr->next=prev;
	return recrev(temp,curr);
}
void recrevwrapper(struct Node** headref)
{
	struct Node *temp,*prev,*curr;
	curr=(*headref);
	prev=NULL;
	(*headref)=recrev(curr,prev);
}

int main()
{	
	struct Node* linkedlist=NULL;
	struct Node** head;
	head = &linkedlist;
	Insert(head,20);
	Insert(head,40);
	Insert(head,60);
	Insert(head,80);
	cout<<"Insert finished";
	traverse(linkedlist);
	cout<<"Reversing using Iterative"<<"\n";
	reverseIterative(head);
	cout<<"Success Iterative!"<<"\n";
	traverse(linkedlist);
	cout<<"Reversing using Recursive"<<"\n";
	recrevwrapper(head);
	cout<<"Success Recursive!"<<"\n";
	traverse(linkedlist);
	return 0;

}