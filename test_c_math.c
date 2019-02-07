/* test_c_math.c */
#include <stdio.h>
#include "c_math.h"

void test_int_square(void)
{
    int x = 10;
    printf("The square of %d is %d.\n", x, int_square(x));

}

int main(int argc, char **argv)
{
    test_int_square();
    return 0;
}
