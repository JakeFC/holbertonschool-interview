#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "sandpiles.h"

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * stability_check - Checks if a sandpile is stable
 * @grid: 3x3 sandpile grid
 * Return: true if stable, false otherwise
 */
static bool stability_check(int grid[3][3])
{
    int y, x;

    for (y = 0; y < 3; y++)
    {
        for (x = 0; x < 3; x++)
        {
            if (grid[y][x] > 3)
                return false;
        }
    }

    return true;
}

/**
 * sandpiles_sum - Computes the sum of two sandpiles and updates grid1
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    int x, y;
    bool stable;
    int tgrid[3][3];

    stable = true;
    for (y = 0; y < 3; y++)
    {
        for (x = 0; x < 3; x++)
        {
            grid1[y][x] += grid2[y][x];
            if (grid1[y][x] > 3)
                stable = false;
        }
    }

    while (!stable)
    {
        puts("=");
        print_grid(grid1);
        stable = true;
        for (y = 0; y < 3; y++)
        {
            for (x = 0; x < 3; x++)
            {
                tgrid[y][x] = grid1[y][x];
            }
        }
        for (y = 0; y < 3; y++)
        {
            for (x = 0; x < 3; x++)
            {
                if (tgrid[y][x] > 3)
                {
                    grid1[y][x] -= 4;
                    if (y > 0)
                        grid1[y - 1][x] += 1;
                    if (y < 2)
                        grid1[y + 1][x] += 1;
                    if (x > 0)
                        grid1[y][x - 1] += 1;
                    if (x < 2)
                        grid1[y][x + 1] += 1;
                }
            }
        }
        stable = stability_check(grid1);
    }
}
