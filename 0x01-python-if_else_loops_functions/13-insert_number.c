#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* insert_node - insert a number to sorted list
* @head: head node
* @number: nymber to be inserted
* Return:  the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *next, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
    		return (NULL);
	new->n = number;
	new->next = NULL;
	next = *head;

	if (*head == NULL || number < (*head)->n)
	{
    		new->next = *head;
    		*head = new;
    		return (new);
	}

	while (next != NULL && number > next->n)
	{
    		prev = next;
    		next = next->next;
	}

	prev->next = new;
	new->next = next;

	return (new);
}
