#include <stdio.h>

int main()
{
    unsigned char arr[] = {'A', 'B', 0, 'C', 'D', '\0', 'E', 'F', NULL};
    printf("%s", arr);
}