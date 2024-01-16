#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	while (f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
