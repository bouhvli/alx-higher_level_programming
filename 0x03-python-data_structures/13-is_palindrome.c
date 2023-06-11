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
	int cmp = 0;
	listint_t *tmp = NULL;
	listint_t *old = *head;

	if (*head == NULL)
		return (1);

	while (old != NULL)
	{
		add_start(&tmp, old->n);
		old = old->next;
	}
	cmp = compare(*head, tmp);
	free_listint(tmp);
	return (cmp);
}
/**
 * add_start - as the name say.
 * @head: takes the list.
 * @value: the value of the element we want to add to @head the list at the
 * 	start.
 * Return: the list or NULL if somthing whent wrong.
 */
listint_t *add_start(listint_t **head, int value)
{
	listint_t *new_node;

	if (*head == NULL)
	{
		*head = add_nodeint_end(head, value);
	}
	else
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node != NULL)
		{
			new_node->n = value;
			new_node->next = *head;
			*head = new_node;
		}
		else
			return (NULL);
	}
	return (*head);
}
/**
 * compare - compare 2 lists and if there is a dif it returns 0 else 1
 * @h: the first list.
 * @t: the second list.
 * Return: 0 if there is a dif and 1 if not
 */
int compare(listint_t *h, listint_t *t)
{
	while (h != NULL && t != NULL)
	{
		if (h->n != t->n)
			return (0);
		h = h->next;
		t = t->next;
	}
	return (1);
}