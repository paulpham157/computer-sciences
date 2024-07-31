// Copyright © 2016-2017 Giovanni Squillero <giovanni.squillero@polito.it>
// https://github.com/squillero/computer-sciences
// Free under certain conditions — see the license for details.

#include <stdio.h>
#include <stdlib.h>

#define ROWS 10
#define COLUMNS 50

int main()
{
    for (int r = 0; r < ROWS; r = r + 1)
    {
        for (int c = 0; c < COLUMNS; c = c + 1)
        {
            if (r == 0 || r == ROWS - 1 ||
                c == 0 || c == COLUMNS - 1 ||
                (r + c) % 3 == 0)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
