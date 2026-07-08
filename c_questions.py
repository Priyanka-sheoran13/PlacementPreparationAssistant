c_questions = [

    {
        "title":"Reverse an Array",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Reverse the elements of an array.",
        "input":"1 2 3 4 5",
        "output":"5 4 3 2 1",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={1,2,3,4,5};

    int i,temp;

    for(i=0;i<5/2;i++){

        temp=a[i];

        a[i]=a[4-i];

        a[4-i]=temp;

    }

    for(i=0;i<5;i++)

        printf("%d ",a[i]);

    return 0;

}"""
    },

    {
        "title":"Largest Element in Array",
        "topic":"Arrays",
        "difficulty":"Easy",
        "description":"Find the largest element in an array.",
        "input":"3 8 2 10 5",
        "output":"10",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={3,8,2,10,5};

    int max=a[0];

    int i;

    for(i=1;i<5;i++){

        if(a[i]>max)

            max=a[i];

    }

    printf("%d",max);

    return 0;

}"""
    },

    {
        "title":"Second Largest Element",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Find the second largest element in an array.",
        "input":"10 20 5 30 25",
        "output":"25",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={10,20,5,30,25};

    int first=-1,second=-1;

    int i;

    for(i=0;i<5;i++){

        if(a[i]>first){

            second=first;

            first=a[i];

        }

        else if(a[i]>second && a[i]!=first)

            second=a[i];

    }

    printf("%d",second);

    return 0;

}"""
    },

    {
        "title":"Palindrome String",
        "topic":"Strings",
        "difficulty":"Medium",
        "description":"Check whether a string is palindrome.",
        "input":"madam",
        "output":"Palindrome",
        "solution":"""#include<stdio.h>
#include<string.h>

int main(){

    char s[]="madam";

    int i,len=strlen(s);

    int flag=1;

    for(i=0;i<len/2;i++){

        if(s[i]!=s[len-i-1]){

            flag=0;

            break;

        }

    }

    if(flag)

        printf("Palindrome");

    else

        printf("Not Palindrome");

    return 0;

}"""
    },

    {
        "title":"Count Vowels",
        "topic":"Strings",
        "difficulty":"Easy",
        "description":"Count vowels in a string.",
        "input":"Programming",
        "output":"3",
        "solution":"""#include<stdio.h>

int main(){

    char s[]="Programming";

    int i,count=0;

    for(i=0;s[i]!='\\0';i++){

        char c=s[i];

        if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||

           c=='A'||c=='E'||c=='I'||c=='O'||c=='U')

            count++;

    }

    printf("%d",count);

    return 0;

}"""
    },

    {
        "title":"Factorial using Recursion",
        "topic":"Recursion",
        "difficulty":"Medium",
        "description":"Find factorial using recursion.",
        "input":"5",
        "output":"120",
        "solution":"""#include<stdio.h>

int fact(int n){

    if(n<=1)

        return 1;

    return n*fact(n-1);

}

int main(){

    printf("%d",fact(5));

    return 0;

}"""
    },

    {
        "title":"Fibonacci using Recursion",
        "topic":"Recursion",
        "difficulty":"Medium",
        "description":"Print nth Fibonacci number.",
        "input":"7",
        "output":"13",
        "solution":"""#include<stdio.h>

int fib(int n){

    if(n<=1)

        return n;

    return fib(n-1)+fib(n-2);

}

int main(){

    printf("%d",fib(7));

    return 0;

}"""
    },

    {
        "title":"Linear Search",
        "topic":"Searching",
        "difficulty":"Easy",
        "description":"Search an element using Linear Search.",
        "input":"10 20 30 40 50",
        "output":"Found",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={10,20,30,40,50};

    int key=30;

    int i;

    for(i=0;i<5;i++){

        if(a[i]==key){

            printf("Found");

            return 0;

        }

    }

    printf("Not Found");

    return 0;

}"""
    },

    {
        "title":"Binary Search",
        "topic":"Searching",
        "difficulty":"Medium",
        "description":"Search an element using Binary Search.",
        "input":"1 3 5 7 9",
        "output":"Found",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={1,3,5,7,9};

    int key=7;

    int low=0,high=4;

    while(low<=high){

        int mid=(low+high)/2;

        if(a[mid]==key){

            printf("Found");

            return 0;

        }

        else if(a[mid]<key)

            low=mid+1;

        else

            high=mid-1;

    }

    printf("Not Found");

    return 0;

}"""
    },

    {
        "title":"Bubble Sort",
        "topic":"Sorting",
        "difficulty":"Medium",
        "description":"Sort an array using Bubble Sort.",
        "input":"5 2 4 1 3",
        "output":"1 2 3 4 5",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={5,2,4,1,3};

    int i,j,temp;

    for(i=0;i<4;i++){

        for(j=0;j<4-i;j++){

            if(a[j]>a[j+1]){

                temp=a[j];

                a[j]=a[j+1];

                a[j+1]=temp;

            }

        }

    }

    for(i=0;i<5;i++)

        printf("%d ",a[i]);

    return 0;

}"""
    },
        {
        "title":"Selection Sort",
        "topic":"Sorting",
        "difficulty":"Medium",
        "description":"Sort an array using Selection Sort.",
        "input":"64 25 12 22 11",
        "output":"11 12 22 25 64",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={64,25,12,22,11};

    int i,j,min,temp;

    for(i=0;i<4;i++){

        min=i;

        for(j=i+1;j<5;j++)
            if(a[j]<a[min])
                min=j;

        temp=a[i];
        a[i]=a[min];
        a[min]=temp;
    }

    for(i=0;i<5;i++)
        printf("%d ",a[i]);

    return 0;
}"""
    },

    {
        "title":"Insertion Sort",
        "topic":"Sorting",
        "difficulty":"Medium",
        "description":"Sort an array using Insertion Sort.",
        "input":"9 5 1 4 3",
        "output":"1 3 4 5 9",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={9,5,1,4,3};

    int i,j,key;

    for(i=1;i<5;i++){

        key=a[i];

        j=i-1;

        while(j>=0 && a[j]>key){

            a[j+1]=a[j];

            j--;

        }

        a[j+1]=key;
    }

    for(i=0;i<5;i++)
        printf("%d ",a[i]);

    return 0;
}"""
    },

    {
        "title":"Matrix Addition",
        "topic":"2D Arrays",
        "difficulty":"Easy",
        "description":"Add two matrices.",
        "input":"2x2 Matrices",
        "output":"Sum Matrix",
        "solution":"""#include<stdio.h>

int main(){

    int a[2][2]={{1,2},{3,4}};
    int b[2][2]={{5,6},{7,8}};
    int c[2][2];
    int i,j;

    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
            c[i][j]=a[i][j]+b[i][j];

    return 0;
}"""
    },

    {
        "title":"Matrix Multiplication",
        "topic":"2D Arrays",
        "difficulty":"Medium",
        "description":"Multiply two matrices.",
        "input":"2x2 Matrices",
        "output":"Product Matrix",
        "solution":"""#include<stdio.h>

int main(){

    int a[2][2]={{1,2},{3,4}};
    int b[2][2]={{5,6},{7,8}};
    int c[2][2]={0};
    int i,j,k;

    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
            for(k=0;k<2;k++)
                c[i][j]+=a[i][k]*b[k][j];

    return 0;
}"""
    },

    {
        "title":"Swap using Pointers",
        "topic":"Pointers",
        "difficulty":"Medium",
        "description":"Swap two numbers using pointers.",
        "input":"10 20",
        "output":"20 10",
        "solution":"""#include<stdio.h>

void swap(int *a,int *b){

    int t=*a;
    *a=*b;
    *b=t;
}

int main(){

    int x=10,y=20;

    swap(&x,&y);

    printf("%d %d",x,y);

    return 0;
}"""
    },

    {
        "title":"Pointer Arithmetic",
        "topic":"Pointers",
        "difficulty":"Medium",
        "description":"Traverse an array using pointers.",
        "input":"1 2 3 4 5",
        "output":"1 2 3 4 5",
        "solution":"""#include<stdio.h>

int main(){

    int a[5]={1,2,3,4,5};

    int *p=a;

    for(int i=0;i<5;i++)
        printf("%d ",*(p+i));

    return 0;
}"""
    },

    {
        "title":"Structure Example",
        "topic":"Structures",
        "difficulty":"Easy",
        "description":"Store student information using structure.",
        "input":"Priyanka 101",
        "output":"Priyanka 101",
        "solution":"""#include<stdio.h>

struct Student{

    char name[20];
    int roll;

};

int main(){

    struct Student s={"Priyanka",101};

    printf("%s %d",s.name,s.roll);

    return 0;
}"""
    },

    {
        "title":"Union Example",
        "topic":"Union",
        "difficulty":"Medium",
        "description":"Demonstrate the use of union.",
        "input":"10",
        "output":"10",
        "solution":"""#include<stdio.h>

union Data{

    int i;
    float f;

};

int main(){

    union Data d;

    d.i=10;

    printf("%d",d.i);

    return 0;
}"""
    },

    {
        "title":"Dynamic Memory Allocation",
        "topic":"malloc()",
        "difficulty":"Medium",
        "description":"Allocate memory using malloc().",
        "input":"5",
        "output":"Memory Allocated",
        "solution":"""#include<stdio.h>
#include<stdlib.h>

int main(){

    int *p;

    p=(int*)malloc(5*sizeof(int));

    if(p!=NULL)
        printf("Memory Allocated");

    free(p);

    return 0;
}"""
    },

    {
        "title":"File Handling",
        "topic":"Files",
        "difficulty":"Medium",
        "description":"Write data into a file.",
        "input":"Hello",
        "output":"File Created",
        "solution":"""#include<stdio.h>

int main(){

    FILE *fp=fopen("data.txt","w");

    fprintf(fp,"Hello");

    fclose(fp);

    printf("File Created");

    return 0;
}"""
    },
        {
        "title":"Singly Linked List Traversal",
        "topic":"Linked List",
        "difficulty":"Medium",
        "description":"Traverse a singly linked list and print all elements.",
        "input":"10 -> 20 -> 30",
        "output":"10 20 30",
        "solution":"""#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

int main(){

    struct Node *head,*second,*third;

    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));

    head->data=10;
    second->data=20;
    third->data=30;

    head->next=second;
    second->next=third;
    third->next=NULL;

    struct Node *temp=head;

    while(temp!=NULL){

        printf("%d ",temp->data);

        temp=temp->next;

    }

    return 0;

}"""
    },

    {
        "title":"Stack using Array",
        "topic":"Stack",
        "difficulty":"Medium",
        "description":"Implement stack using array.",
        "input":"Push 10,20,30",
        "output":"30 20 10",
        "solution":"""// Stack using Array in C"""
    },

    {
        "title":"Queue using Array",
        "topic":"Queue",
        "difficulty":"Medium",
        "description":"Implement queue using array.",
        "input":"10 20 30",
        "output":"10 20 30",
        "solution":"""// Queue using Array in C"""
    },

    {
        "title":"Circular Queue",
        "topic":"Queue",
        "difficulty":"Hard",
        "description":"Implement Circular Queue.",
        "input":"Queue Operations",
        "output":"Circular Queue",
        "solution":"""// Circular Queue Implementation"""
    },

    {
        "title":"Binary Search Tree",
        "topic":"Trees",
        "difficulty":"Hard",
        "description":"Insert elements into Binary Search Tree.",
        "input":"10 5 20",
        "output":"Inorder Traversal",
        "solution":"""// Binary Search Tree in C"""
    },

    {
        "title":"Merge Two Arrays",
        "topic":"Arrays",
        "difficulty":"Easy",
        "description":"Merge two arrays.",
        "input":"1 2 3 + 4 5 6",
        "output":"1 2 3 4 5 6",
        "solution":"""// Merge Arrays Program"""
    },

    {
        "title":"Remove Duplicates",
        "topic":"Arrays",
        "difficulty":"Medium",
        "description":"Remove duplicate elements from an array.",
        "input":"1 2 2 3 4 4",
        "output":"1 2 3 4",
        "solution":"""// Remove Duplicates Program"""
    },

    {
        "title":"Prime Number",
        "topic":"Math",
        "difficulty":"Easy",
        "description":"Check whether a number is prime.",
        "input":"17",
        "output":"Prime",
        "solution":"""// Prime Number Program"""
    },

    {
        "title":"Armstrong Number",
        "topic":"Math",
        "difficulty":"Medium",
        "description":"Check whether a number is an Armstrong number.",
        "input":"153",
        "output":"Armstrong",
        "solution":"""// Armstrong Number Program"""
    },

    {
        "title":"Reverse Number",
        "topic":"Math",
        "difficulty":"Easy",
        "description":"Reverse a given number.",
        "input":"12345",
        "output":"54321",
        "solution":"""// Reverse Number Program"""
    }

]