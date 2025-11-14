/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
//Lab 1


#include <stdio.h>
#include <cstdlib>
#include <iostream>
using namespace std;

void fillArray_1D(int array[], int size){
    for(int i = 0; i < size; i++) {
        array[i] =(rand() % 100);
    }
}

void fillArray_2D(int array[3][3]){
 
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            array[i][j] = (rand() % 100);
         }
     }
}

void fillArray_2D(int array[3][4]){
 
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 4; j++) {
            array[i][j] = (rand() % 100);
         }
     }
}

void printArray_1D(int array[], int n){
    for(int i=0; i<n; i++)
    {
        cout<<array[i]<<" ";
    }
}
void printArray_2D(int array[3][3]) {
     for(int i = 0; i < 3; i++) {
         for(int j = 0; j < 3; j++) {
             cout<<"\t"<<array[i][j];
     }
    cout<<"\n";
    }
}

void printArray_2D(int array[3][4]) {
     for(int i = 0; i < 3; i++) {
         for(int j = 0; j < 4; j++) {
             cout<<"\t"<<array[i][j];
        }
     cout<<"\n";
    }
}

double belowAboveAverage (int array[],int size) 
{
    double sum = 0, average = 0;
    int count = 0;
    int small =0, larg =0;

    
         for (int i =0; i< size; i++) 
         {
               sum+=array[i];
        }
     average = sum/size;
     cout<<"The average of all elements of the array is: "<<average<<"\n";

         for (int i =0; i< size; i++){
              if (array[i]<average){
                   small++;
         } 
             else if (array[i]>average){
                larg++;
         }
        
        }
        cout<<"\nThe Number of elements that are less than the average is: "<<small<<"\n";
        cout<<"\nThe elements that are less than the average are: \n";
         for(int i=0;i<size;i++){
            
            if (array[i]<average){
                cout<<array[i]<<"  ";
            } 
            
        }
        
        cout<<"\n\n\nThe Number of elements that are greater than the average is: "<<larg<<"\n";
        cout<<"\nThe elements that are greater than the average are: \n";
         for(int i=0;i<size;i++){
            
            if (array[i]>average){
                cout<<array[i]<<"  ";
            } 
            
        }
    return average;
}

void swapLagestSmallest(int array[], int size){
    
    int smallest=array[0], largest=array[size-1], min= 0, max= 0;
    
    cout<<"Before swapping the elements:\n";
    cout<<"The elements of the array are as followd:\n";
    for(int i=0; i<size;i++){
        cout<<array[i]<<"  ";
        
        if(array[i]<smallest){
            smallest=array[i];
            min=i; 
        }
        else if(array[i]>largest){
            largest=array[i];
            max=i;
        }
        }
        cout<<"\n";
        cout<<"\nLargest element of the array is: "<<largest<<"\n";
        cout<<"\nSmallest element of the array is: "<<smallest<<"\n";
        cout<<"\nAfter swapping the elements: "<<"\n";
        cout<<"The elements of the array are as followd:\n";
        
        int index=array[min];
        array[min]=array[max];
        array[max]=index;
        
        for(int i=0; i<size; i++){
            cout<<array[i]<<"  ";
        }
}

int sumRow(int array[3][3],int row){
 int sum=0;
 for(int i=0; i<3; i++){
    sum+=array[row][i];
 }
 return sum;
}
int sumColumn(int array[3][3],int column){
 int sum=0;
 
    for(int i=0; i<3; i++){
 sum+=array[i][column];
 }
 return sum;
}

void sumRowsColumns(int array[3][3]){
 cout<<"The elements of the array with the sum of rows and column are as followd :\n\n";
 for(int i=0; i<3; i++){
    cout << "\t";
    for ( int j=0;j<3;j++){
        cout << array[i][j] << "\t";
    }
    cout<<"sum :"<<sumRow(array,i)<<"\n";
 }
 cout<<"sum :  ";
 for(int i=0; i<3; i++){
    cout<<sumColumn(array,i)<<"\t";
 }
}

void repeatedElementsRow(int array[3][4]){
 int sum;
 bool check = false;
      for(int i=0; i<3; i++){
        for(int j=i+1; j<4; j++){
 
          if(array[3][i]==array[3][j]){
             check = true;
             }
             
        }
 }
 
    if (!check){
        cout<< "\nno row contains dublicate elements\n";
    }
 
}

int main()
{
 int array_size;
 cout<<"**************************************************\n";
 cout<<"*****************ARRAY exercise*****************\n";
 cout<<"**************************************************\n";
 cout<< "\n\nTasks related to 1-D";
 cout<< "\nHow mnay elemnts of the 1D array? ";
 cin>> array_size;
 
 int array1[array_size];
 
 fillArray_1D(array1,array_size);
 
 cout<< "\nElemnts of array are as follows:\n";
 printArray_1D(array1,array_size);
 
 cout<< "\n\n\nTask 1:\n";
 belowAboveAverage(array1, array_size);
 
 cout<< "\n\n\nTask 2:\n";
 swapLagestSmallest(array1, array_size);
 
 
 cout<< "\n\n\nTasks related to 2-D\n\n";
 
 int array2[3][3];
 cout<<"Entering random numbers in array of 3 rows and 3 columns:\n";
 fillArray_2D(array2);
 printArray_2D(array2);
 
 cout<< "\n\nTask 3:\n";
 sumRowsColumns(array2);
 
 cout<< "\n\n\nTask 4:\n";
 int array3[3][4];
 cout<<"Entering random numbers in array of 3 rows and 4 columns:\n";
 fillArray_2D(array3);
 printArray_2D(array3);
 repeatedElementsRow(array3);
 return 0;
}
