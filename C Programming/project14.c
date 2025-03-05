#include <stdio.h>

int main()
{
    unsigned char arr[] = {'A', 'B', 'C', 'D', 'E', 'F', NULL};
    long *ptr = arr;
    printf("%c", ptr[1]);
}
