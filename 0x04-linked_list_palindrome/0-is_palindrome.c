#include "lists.h"

/**
 * fix_list - fixes a singly linked list previously broken by is_palindrome
 * @one: pointer to first node in first singly linked list
 * @middle: middle pointer of an odd-numbered list
 * @two: pointer to the first node in second isngly linked list
 * Return: 1 if list was a palindrome, 0 if not
 */
int fix_list(listint_t **one, listint_t **middle, listint_t **two)
{
	listint_t *o_current, *t_current, *t_next, *t_previous = NULL;
	int result = 1;

	o_current = *one;
	t_current = *two;
	while (o_current->next)
	{
		if (o_current->n != t_current->n)
			result = 0;
		o_current = o_current->next;
		t_next = t_current->next;
		t_current->next = t_previous;
		t_previous = t_current;
		t_current = t_next;
	}
	if (o_current->n != t_current->n)
		result = 0;
	t_current->next = t_previous;
	if (*middle)
		o_current->next = *middle;
	else
		o_current->next = t_current;
	return (result);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to first node in singly linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *previous, *current, *next, *middle;
	int x, size = 0;

	if (!*head)
		return (1);
	current = *head;
	if (!current->next)
		return (1);
	while (current)
	{
		size++;
		current = current->next;
	}
	current = *head;
	for (x = 0; x < (size / 2) - 1; x++)
	{
		current = current->next;
		next = current->next;
	}
	middle = NULL;
	current->next = NULL;
	if (size % 2)
	{
		middle = next;
		current = next->next;
	}
	else
		current = next;
	for (x = (size + 1) / 2, previous = NULL; x < size; x++)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	return (fix_list(head, &middle, &previous));
}
