#include <stdio.h>
#include <stdlib.h>

int min(int a, int b)
{
    return a < b ? a : b;
}

int max(int a, int b)
{
    return a > b ? a : b;
}

int main()
{
    int max_n = 0;
    int min_n = 11;
    int number;
    char line[30];
    while (1)
    {
        scanf("%d", &number);
        if (number == 0)
        {
            return 0;
        }
        scanf("%s", line);
        switch (line[4])
        {
        case 'h':
            max_n = max(max_n, number);
            break;
        case 'l':
            min_n = min(min_n, number);
            break;
        case 't':
            if (number > max_n || number < min_n)
            {
                printf("Stan may be honest");
            }
            else
            {
                printf("Stan is dishonest");
            };
            max_n = 0;
            min_n = 11;
        }
    }
    return 0;
}
// l h t