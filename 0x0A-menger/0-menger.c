#include "menger.h"

/**
 * createSizesArray - fills the array of given level with the size of each
 * square which makes up the Menger Sponge
 *
 * @level: what level Menger Sponge this is
 */
int *createSizesArray(int level)
{
	int *squareSizes, i;

	if (level == 0)
		return (NULL);
	squareSizes = (int *)malloc(sizeof(int) * level);
	for (i = 0; level > 0; i++, level--)
	{
		squareSizes[i] = pow(3, level);
	}
	return (squareSizes);
}

/**
 * isValidCoordinate - Checks if a coordinate is valid or empty in a Menger
 * Sponge
 *
 * @x: x coordinate to check
 * @y: y coordinate to check
 * @level: the level of the Menger Sponge
 * @squareSizes: array containing each size of square in the sponge
 * Return: true if valid, false if empty
 */
bool isValidCoordinate(int x, int y, int level, int *squareSizes)
{
	int i;

	for (i = 0; i < level; i++)
	{
		if ((x + 1) % squareSizes[i] <= squareSizes[i] - squareSizes[i] / 3 &&
			(x + 1) % squareSizes[i] > squareSizes[i] - 2 * squareSizes[i] / 3 &&
			(y + 1) % squareSizes[i] <= squareSizes[i] - squareSizes[i] / 3 &&
			(y + 1) % squareSizes[i] > squareSizes[i] - 2 * squareSizes[i] / 3)
			return (false);
	}
	return (true);
}

/**
 * menger - Draws a 2D Menger Sponge of given level
 *
 * @level: level of the Menger Sponge to draw
 */
void menger(int level)
{
	int x, y, size, *squareSizes;

	if (level < 0)
		return;
	if (level == 0)
	{
		puts("#");
		return;
	}
	squareSizes = createSizesArray(level);
	size = pow(3, level);
	for (y = 0; y < size; y++)
	{
		for (x = 0; x < size; x++)
		{
			if (isValidCoordinate(x, y, level, squareSizes))
				putchar('#');
			else
				putchar(' ');
		}
		putchar('\n');
	}
	free(squareSizes);
}
