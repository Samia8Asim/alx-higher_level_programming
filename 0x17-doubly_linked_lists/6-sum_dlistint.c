#include "lists.h"

/**
 * sum_dlistint - function that returns the sum of all the data
 * @head: head of list
 * Return: the sum of all the data in list
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	while (head != NULL)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}
