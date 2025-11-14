/******************************************************************************

//lab 9

*******************************************************************************/
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <stack>

using namespace std;
class QueueNode {
    
    private:
    int data;
    QueueNode* next;
    
    public:
    // CONSTRUCTORS
    QueueNode() {
        data = 0;
        next = NULL;
    }
    QueueNode(int data) {
        this->data = data;
        next =NULL;
    }
    QueueNode(int data, QueueNode* next) {
        this->data = data;
        this->next = next;
    }
        
    int getData() {
        return data;
    }
    
    QueueNode* getNext() {
        return next;
    }
    
    
    void setData(int data) {
        this->data = data;
    }
    
    void setNext(QueueNode* next) {
        this->next = next;
    }
};

class QueueLL {

    private:
    QueueNode* front;
    QueueNode* back;
    
    public:
    
    //CONSTRUCTOR
    
    QueueLL() {
    front = NULL ;
    back = NULL;
    }
    
    bool isEmpty() {
        return front == NULL;
    }
    
    void printQueue(){
        
        QueueNode* helpPtr = front;
        
        while (helpPtr != NULL) {
            
            cout<<helpPtr->getData()<<", ";
            helpPtr = helpPtr->getNext();
        }
        cout<<endl;
    }
    void enqueue(int data) {

        QueueNode* temp = new QueueNode(data);
        
        
        if (isEmpty()) {
            front = back = temp; 
        }
        else{
            back->setNext(temp);
            back = back->getNext();
        }
    }
    QueueNode* dequeue() {
        
        QueueNode* temp = front;
        front = front->getNext();
        
        if (front == NULL) {
             back = NULL; }
             
        temp->setNext(NULL);
        
         return temp; 
    }
    
    int peek() {
        
        int frontValue = front->getData();
        return frontValue;
    }
    
    void SmallestLargest() {
        
        cout<<"\tDisplaying smallest and lasgest nodes: \n";
        int smallest = front->getData();
        int largest = front->getData();
        
        QueueNode* helpPtr = front;
        
        while (helpPtr != NULL) {
            if (smallest > helpPtr->getData()) {
                smallest = helpPtr->getData();
            }
            if (largest < helpPtr->getData()) {
                largest = helpPtr->getData();
            }
            helpPtr = helpPtr->getNext();
        }
        cout<<endl;
        cout<<"\tSmallest element in the queue is "<<smallest;
        cout<<"\n\tlargest element in the queue is " <<largest;
        cout<<endl;
    }
    QueueLL* fillQWithRandomNumber(QueueLL* myQueue){
        srand(time(0));
        
        int value=0;
        
        for(int i=0;i<10;i++){
            
            value= (rand() % 1000);
            myQueue-> enqueue ( value );
        }
        return myQueue;
        
    }
    
    QueueLL* deleteNode(QueueLL* myQueue, int data){
        
       QueueLL* queue1=myQueue;
       QueueLL* queue2=new QueueLL();
       QueueLL* queue3=new QueueLL();
       
       for(int i=0; i<10; i++){
           if(queue1->peek()!= data){
               
               queue2->enqueue(queue1->peek());
               queue1->dequeue();
              
           }else{
               queue3->enqueue(queue1->peek());
               queue1->dequeue();
           }
       }
       
       cout<<"\tAfter deleting the value "<<queue3->peek()<<" , element of queue 1 are as the following\n";
       cout<<"\t";
       queue2->printQueue();
       cout<<endl;
       return queue2;
    }
    void OddEvenNode(QueueLL* myQueue){
        
       QueueNode* temp=front;
       QueueLL* evenQue=new QueueLL();
       QueueLL* oddQue=new QueueLL();
       
       cout<<"\tElement of queue 1 are as following:\n";
       cout<<"\t";
       myQueue->printQueue();
       cout<<endl;
       
       while(temp!=NULL){
           int value=temp->getData();
           
           if(value%2==0){
               
               evenQue->enqueue(value);
              
           }else{
               oddQue->enqueue(value);
           }
           temp=temp->getNext();
       }
       
       cout<<"\tElement of queue 2 are as following:\n";
       cout<<"\t";
       evenQue->printQueue();
       cout<<endl;
       
       cout<<"\tElement of queue 3 are as following:\n";
       cout<<"\t";
       oddQue->printQueue();
       cout<<endl;
    }
    void reveresElement(QueueLL* myQueue){
        cout<< "\tElements of queue are as the following:\n";
        cout<<"\t";
        myQueue->printQueue();
        cout<<endl;
        
        stack <int> st;
        
        QueueNode* temp =front;
        
        while (!myQueue->isEmpty()){
            st.push(myQueue->peek());
            myQueue->dequeue();
        }
        while(!st.empty()){
            myQueue->enqueue(st.top());
            st.pop();
        }
        cout<<"\tElement of the queue after reversing are as following:\n";
        cout<<"\t";
        myQueue->printQueue();
        
    }
    
    
 };//end of class


int main()
{
    
    int value; 
    
    QueueLL* testQueue = new QueueLL();
    QueueLL* myQueue = new QueueLL();
    
   
    cout<<"\tWhat are values do you want to enqueue ( the input ends if it is 0): ";
    cin>>value;
    
    while (value != 0) {
        
        testQueue->enqueue(value);
        cout<<"\t "<<value<< " was successfully enqueued into the queue.";
        cin>>value;
    }
    cout<<endl;
    
    if (testQueue->isEmpty()) {
        
        cout<<"\tError: cannot print nodes (the queue is empty)";
    } else {
        
        cout<<"\tPrinting All Nodes:\n";
        cout<<" ";
        cout<<"\t";
        testQueue->printQueue();
    }
    
    testQueue->SmallestLargest();
    
    myQueue->fillQWithRandomNumber(myQueue);
    
    cout<<endl;
    cout<<"\t>>>>>>>> Delete Node from the queue (using 2nd queue) <<<<<<<<";
    cout<<endl;
    cout<<"\tBefore deleting value, elements of the queue are as following:\n";
    cout<<"\t";
    myQueue->printQueue();
    cout<<endl;
    
    cout<<"\tPlease enter an int value to delete: ";
    cin>>value;
    myQueue=myQueue->deleteNode(myQueue,value);
    cout<<endl;
    
    cout<<endl;
    cout<<"\t>>>>>>>> Even and odd value queues <<<<<<<<\n";
    myQueue->OddEvenNode(myQueue);
    
    cout<<endl;
    cout<<"\t>>>>>>>> Reverse the elements of a queue <<<<<<<<\n";
    cout<<endl;
    myQueue->reveresElement(myQueue);
    
    
    cout<<endl;



    return 0;
}
