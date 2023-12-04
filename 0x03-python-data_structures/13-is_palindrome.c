#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverseList - function to reverse linked List
 * @head: head of the list
 * Return: reversed list
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL, *current = head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p = *head, *q = *head;
	listint_t *first_half, *sec_half, *sec_half_rev;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (1)
	{
		if (p->next == NULL)
		{
			sec_half = q->next->next;
			break;
		}
		else if (p->next->next == NULL)
		{
			sec_half = q->next;
			break;
		}
		p = p->next->next;
		q = q->next;
		if (p == NULL || p->next == NULL)
			return (1);
	}
	q->next = NULL;
	sec_half_rev = reverseList(sec_half);
	first_half = *head;

	while (sec_half_rev != NULL)
	{
		if (sec_half_rev->n != first_half->n)
			return (0);
		sec_half_rev = sec_half_rev->next;
		first_half = first_half->next;
	}
	return (1);
}
