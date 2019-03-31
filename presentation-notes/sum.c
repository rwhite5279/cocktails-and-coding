# include <stdio.h>

int main(void)
{
    int x, sum;
    sum = 0;
    x = 1;
    while (x < 256)
    {
        printf("%d ",x);
        sum = sum + x;
        x = x + 1;
    }
    printf("\nSum = %d\n", sum);
}
