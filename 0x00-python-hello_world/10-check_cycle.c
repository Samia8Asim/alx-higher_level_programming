#include "lists.h"
#include <unistd.h>
#include <stdio.h>


/**
* check_cycle - function to ckeck fot linked list cycle
* @list: input list
* Return: 0 if no cycle found and 1 otherwisr
*/

int check_cycle(listint_t *list)
{
	listint_t *now_node = list;
	listint_t *next_node = list;

	while (next_node != NULL && next_node->next != NULL)
	{
		now_node = now_node->next;
		next_node = next_node->next->next;

		if (now_node == next_node)
			return (1);
	}
	return (0);
}
