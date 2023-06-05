#include "lists.h"
/**
 * check_cycle - this function will check if the
 * linked list has a cylce or not.
 * @list: the list we wanted to check.
 * Return: 1 if there is a cycle and 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *c;
	listint_t *upNext;

	if (list == NULL)
		return (0);
	c = list;
	upNext = list->next;
	while (c != NULL && upNext != NULL)
	{
		if (c != upNext)
		{
			c = c->next;
			upNext = upNext->next;
			if (upNext != NULL)
				upNext = upNext->next;
			else
				return (0);
		}
		else
		{
			return (1);
		}
	}
	return (0);
}
