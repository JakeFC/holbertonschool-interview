#include "slide_line.h"

/**
 * slide_line - Slides and merges an array of integers.
 *
 * @line: Pointer to array of integers.
 * @size: Number of elements in the array.
 * @direction: Direction argument of SLIDE_LEFT or SLIDE_RIGHT value.
 * Return: 1 on success, 0 on failure.
 */
int slide_line(int *line, size_t size, int direction)
{
	int current, previous, start, end, increment;

	if (!line)
		return (0);
	if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
		return (0);
	increment = direction == SLIDE_LEFT ? 1 : -1;
	start = direction == SLIDE_LEFT ? 0 : size - 1;
	/* End must be beyond the array to avoid 2 functions */
	end = direction == SLIDE_LEFT ? (int)size : -1;
	for (current = start; current != end; current += increment)
	{
		if (current == start)
			previous = current;
		else if (line[current] != 0)
		{
			if (line[current] == line[previous])
			{
				/* Same numbers add together once, so increment after. */
				line[previous] += line[current];
				line[current] = 0;
				previous += increment;
			}
			else if (line[previous] == 0)
			{
				/* Replace a zero while saving the index for later adding. */
				line[previous] = line[current];
				line[current] = 0;
			}
			else
			{
				/* Index after previous is 0 or current, so this works. */
				previous += increment;
				line[previous] = line[current];
				if (previous != current)
					line[current] = 0;
			}
		}
	}
	return (1);
}
