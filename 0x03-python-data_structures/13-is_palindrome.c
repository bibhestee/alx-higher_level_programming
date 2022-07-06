#include "lists.h"
#include <stdlib.h>

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

/**
 * checker - checks if its palindrome or not
 * @list: singly linked list data
 * @i: length of the linked list
 *
 * Return: return 1 if palindrome or 0 if not
 */

int checker(int list[], int i)
{
	if (i != 1)
	{
		int half_l = i / 2;
		int x;

		i--;
		for (x = 0; x != half_l; x++, i--)
		{
			if (list[x] == list[i])
			{
				continue;
			}
			else {
				return (0);
			}
		}
		return (1);
	}
	else {
		return (0);
	}
}

