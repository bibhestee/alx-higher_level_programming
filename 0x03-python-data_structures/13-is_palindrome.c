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

	return (rev_list(list, i));
}

/**
 * rev_list - Reverse the list and checks if its a palindrome
 * @list: singly linked list
 * @size: list length
 *
 * Return: returns 1 if its a palindrome or 0 if not.
 */
int rev_list(int list[], int size)
{
	int new_list[size];

	/* Reverse the list and store in new list */
	for (int i = size - 1, j = 0; i >= 0; i--, j++)
	{
		new_list[j] = list[i];
	}

	/* Check if its a palindrome */
	for (int i = 0; i < size; i++)
	{
		if (new_list[i] == list[i])
			continue;
		else
		{
			return (0);
		}
	}
	return (1);
}
