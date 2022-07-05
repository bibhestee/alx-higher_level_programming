
#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to the linked list
 *
 * Return: 1 if its a palindrome or 0 if not
 */

int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int i = 0;
	int list[30];

	current = *head;

	while (current != NULL)
	{
		list[i] = current->n;
		current = current->next;
		i++;
	}

	return (checker(list, i));
}

int checker(int list[], int i)
{
	int half_l = i / 2;
	i--;
	for (int x = 0; x != half_l; x++, i--)
	{
		if (list[x] == list[i])
		{
			printf("%i : %i\n", list[x], list[i]);
			continue;
		}
		else {
			return (0);
		}
	}
	return (1);
}

