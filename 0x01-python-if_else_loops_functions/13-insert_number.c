#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - this function will insert into a sorted list.
 * @head: the list.
 * @number: the number we want to insert.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *suiv, *prev;

	if (head == NULL)
		return (add_nodeint_end(head, number));

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	suiv = (*head)->next;
	prev = *head;

	while (suiv)
	{
		if (suiv->n > number)
		{
			prev->next = new;
			new->next = suiv;
			break;
		}
		prev = suiv;
		suiv = suiv->next;
	}
	if (suiv == NULL)
	{
		add_nodeint_end(head, number);
		free(new);
	}
	return (new);
}
/**
 * add_node - add a new node to the start of the list.
 * @head: the list.
 * @n: the number we want to insert.
 * Return: null in case of error or the address of the new node.
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint_t *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = n;
	newnode->next = *head;
	*head = newnode;

	return (newnode);
}
