#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stdbool.h>
/**
 * is_palindrome - checks if a list of number if palindrome.
 * @head: the list we want to check.
 * Return: 0 if it is not palindrome and 1 if yes.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL;
	int table[4500];
	int idx = 0, idxrev = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	if (tmp->next == NULL)
		return (0);
	while (tmp)
	{
		table[idx] = tmp->n;
		tmp = tmp->next;
		if (tmp != NULL)
			idx++;
	}
	while (idx > 0 && idxrev <= idx)
	{
		if (table[idx] != table[idxrev])
			return (0);
		idx--, idxrev++;
	}
	return (1);
}
