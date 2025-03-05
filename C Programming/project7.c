#include <stdio.h>

void main()
{
    int num1;
    int num2;
    char operator;
    printf("Enter number 1 : ");
    scanf("%i", &num1);

    printf("Enter oprator : ");
    scanf("%s", &operator);

    printf("Enter number 2 : ");
    scanf("%i", &num2);

    if (operator== '+')
    {
        printf("The addition is = %i  \n", num1 + num2);
    }
    else if (operator== '*')
    {
        printf("The multiblecation is = %i \n", num1 * num2);
    }
    else if (operator== '-')
    {
        printf("The subtration is = %i \n", num1 - num2);
    }
    else if (operator== '/')
    {
        printf("The divinison is = %i  \n", num1 / num2);
    }
    else if (operator== '%')
    {
        printf("The result  is = %i \n", num1 % num2);
    }
}