#include <stdlib.h>
#include <stdio.h>
#include "palindrome.h"

/**
 * is_palindrome - checks whether or not a given unsigned int is a palindrome
 * @n: unsigned integer to be checked
 * Return: 1 if n is a palindrome, otherwise 0
 */
int is_palindrome(unsigned long n)
{
	int array[20], i, end;

	for (i = 0; n > 0; n /= 10, i++)
	{
		/*
		* the digits are saved into the array in reverse, but it doesn't matter
		*/
		array[i] = n % 10;
	}
	end = i - 1;
	for (i = 0; i <= end; i++, end--)
	{
		if (array[i] != array[end])
			return (0);
	}
	return (1);
}
