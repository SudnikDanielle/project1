#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b;
    scanf("%d",&a);
    printf("%d \n", (-3<=a)&&(6>=a));
    scanf("%d",&b);
    if (b&(1<<5))
    {
        printf("1");
    }
    else
    {
        printf("0");
    }
    return 0;
}
