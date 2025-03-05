#include <stdio.h>

int main()
{
    unsigned char v = 0x34;

    if (v)
    {
        printf("1");
    }
    if (!v)
    {
        printf("2");
    }
    if (~v)
    {
        printf("3");
    }

    v = 0xFF;

    if (!v)
    {
        printf("4");
    }
    if (~v)
    {
        printf("5");
    }

    v = 0x00;

    if (!v)
    {
        printf("6");
    }
    if (~v)
    {
        printf("7");
    }

    return 0;
}
