/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

//lab 3
#include <iostream>

using namespace std;
struct node
{
    int data;
    node *next;
};

void printAllNodes(node *head) {
    node *temp = new node();
    temp= head;
    while (temp != NULL) {
     cout<<"\nvalues of node: "<<temp->data;
     temp = temp->next ;
    }
}

int findLargest(node* head) {
  node *temp = new node();
  temp= head;
  
  int max=head->data;
   while (temp != NULL) {
       if(temp->data > max){
           max=temp->data;
       }
       temp= temp->next;
   }
   return max;
  
}

node* data2ndNode (node* head){
   node *sec = new node();
   sec= head->next;
  
   return sec;
 }
 
node* data2ndLastNode (node* head ){
    node *temp = new node();
    node* last = new node();
    
    last = head;
    temp = head -> next;
   
    while(temp->next != NULL){
        last = last -> next;
        temp= temp->next;
        
        if(temp->next== NULL){
            temp = last;
            return temp;
        }
    }
    return temp;
}
void deleteLastNode (node* head){ 
    node *temp = new node();
    node *last = new node();
    
    last =head;
    temp = head;
    while (temp->next != NULL) {
        last =temp;
        temp = temp ->next;
    }
    last-> next=NULL;
    temp =NULL;
}

void odd2Even2Odd (node* head){
    node *temp = new node();
    temp =head;
    int r,num;
    
    while (temp != NULL) {
        r=temp -> data;
        num=r%2;
        
        if(num==0){
          r++;
          temp->data=r;
          
        }
        else if(num!= 0){
            r--;
             temp->data=r;
        }
        temp=temp->next;
    }
    
}
int main()
{
    node* n1= new node();
    node* n2= new node();
    node* n3= new node();
    node* n4= new node();
    
    n1-> data=10;
    n1-> next=n2;
    
    n2-> data=21;
    n2-> next=n3;
    
    n3-> data=6;
    n3-> next=n4;
    
    n4-> data=8;
    n4-> next=NULL;
    
    printAllNodes(n1);
    
    cout<<"\nthe largest number: "<<findLargest(n1);
    cout<<"\nthe second node value: "<<data2ndNode(n1)->data;
    cout<<"\nthe last node value: "<<data2ndLastNode(n1)->data;
    
    deleteLastNode(n1);
    cout<<"\nthe delete last node  ";
    
    printAllNodes(n1);
    odd2Even2Odd(n1);
    
    cout<<"\n modifying the nodes values by using odd2Even2Odd method: ";
    
    printAllNodes(n1);
    
    
    return 0;
}
