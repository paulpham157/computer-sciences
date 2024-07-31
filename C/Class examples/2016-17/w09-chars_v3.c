// Copyright © 2016-2017 Giovanni Squillero <giovanni.squillero@polito.it>
// https://github.com/squillero/computer-sciences
// Free under certain conditions — see the license for details.

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    for (int t = 0; t < 10; ++t)
    {
        int c = getchar();
        // toupper()
        if (c >= 'a' && c <= 'z')
        {
            int pos = c - 'a';
            printf("%c\n", 'A' + pos);
        }
        else
        {
            printf("%c\n", c);
        }
    }
    return EXIT_SUCCESS;
}
