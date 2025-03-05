#include <stdio.h>

int add(int x, int y)
{
    int result = x + y;
    return result;
}

int main()
{
    printf("%d", 20 / add(2, 3) * 4);
    return 0;
}
