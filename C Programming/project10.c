#include <stdio.h>

int main()
{
    int diameter = 101;
    int half = diameter / 2;
    int i, j;
    for (i = 0; i <= half; i++)
    {
        for (j = 0; j < half - i; j++)
        {
            printf(" ");
        }
        for (j = 0; j < 2 * i + 1; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (i = half - 1; i >= 0; i--)
    {
        for (j = 0; j < half - i; j++)
        {
            printf(" ");
        }
        for (j = 0; j < 2 * i + 1; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}
