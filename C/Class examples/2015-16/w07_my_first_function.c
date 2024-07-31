// Copyright © 2015-2016 Giovanni Squillero <giovanni.squillero@polito.it>
// https://github.com/squillero/computer-sciences
// Free under certain conditions — see the license for details.

#include <stdio.h>
#include <stdlib.h>

/* PROTO */
float AddOne(int foo);

int MyRandom(void)
{
    return rand() % 42;
}

void MyDebug(int x)
{
    printf("Grand 'ma debug: %d\n", x);
    return;
}

int main(void)
{
    int baz, quz;

    baz = 42;
    quz = AddOne(baz - 1);

    printf("baz: %d -- quz: %d\n", baz, quz);
    return 0;
}

float AddOne(int foo)
{
    float baz;
    baz = foo + 1.0;
    return baz;
}
