#include "lists.h"

/**
 * add_dnodeint_end - adds a new node at the end of a dlistint_t list.
 * @head: head of list
 * @n: int in end_node
 * Return:  address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *end_node, *current;

	end_node = malloc(sizeof(dlistint_t));
	if (end_node == NULL)
		return (NULL);

	end_node->n = n;
	end_node->next = NULL;
	current = *head;
	if (*head == NULL)
	{
		*head = end_node;
		end_node->prev = NULL;
		return (end_node);
	}
	while (current->next != NULL)
	{
		current = current->next;
	}
	end_node->prev = current;
	current->next = end_node;
	return (end_node);
}
