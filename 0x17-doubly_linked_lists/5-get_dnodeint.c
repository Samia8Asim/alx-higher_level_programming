#include "lists.h"

/**
 * get_dnodeint_at_index -  returns the nth node of list
 * @head: head of list
 * @index: index of nth node
 * Return: the nth node of list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current = head;
	unsigned int count = 0;

	if (head == NULL)
		return (NULL);
	while (current != NULL)
	{
		if (count == index)
			return (current);
		count++;
		current = current->next;
	}
	return (NULL);
}
