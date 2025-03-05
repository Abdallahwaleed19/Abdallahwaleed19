#include <stdio.h>

void main()
{
    char name[10];
    printf("Enter your full name : ");
    scanf("%s", &name);
    printf("My name is %s \n ", name);

    int age;
    printf("Enter your age : ");
    scanf("%d", &age);
    printf("My age is %d \n ", age);
}