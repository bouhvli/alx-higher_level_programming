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
	listint_t *tmp = *head;
	listint_t *lsit = NULL;
	listint_t *revl = NULL;
	int size = size_of(tmp), i = 0;

	if (*head == NULL)
		return (1);
	while (i < (size / 2))
	{
		add_nodeint_end(&lsit, tmp->n);
		tmp = tmp->next;
		i++;
	}
	while (i < size)
	{
		revl = add_start(&revl, tmp->n);
		tmp = tmp->next;
		i++;
	}
	i = 0;
	while (i < (size / 2))
	{
		if(revl->n != lsit->n)
			return (0);
		revl = revl->next;
		lsit = lsit->next;
		i++;
	}
	return (1);
}
/**
 * size_of - determine the size of a lidt.
 * @h: the list head.
 * Return: the number of elements in a list.
*/
int size_of(listint_t *h)
{
	listint_t *tmp = h;
	int count = 0;

	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}
/**
 * add_start - as the name say.
 * @head: takes the list.
 * @value: the value of the element we want to add to @head the list at the
 * 	start.
 * Return: the list or NULL if somthing whent wrong.
 */
listint_t *add_start(listint_t **head, const int value)
{
	listint_t *new_node = NULL;

	if (*head == NULL)
		*head = add_nodeint_end(head, value);
	else 
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = value;
		new_node->next = *head;
		*head = new_node;
	}
	return (*head);
}
