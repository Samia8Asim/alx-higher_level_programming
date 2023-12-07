#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked list
 * @h: head
 * Return: returns the number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t num_elements = 0;

	while (h != NULL)
	{
		num_elements++;
		h = h->next;
	}
	return (num_elements);
}
