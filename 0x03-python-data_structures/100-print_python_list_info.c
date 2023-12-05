#include <stdio.h>
#include <stdlib.h>

/**
 * struct  elements - singly linked list
 * @str: string
 * @inti: int
 *
 * Description: singly linked list node struct
 */
typedef struct elements
{
	char *str;
	int inti;
} Elements;

/**
 * struct pyop - singly linked list
 * @size: size of list
 * @allocated: allocated memory
 * @element: elements in list
 *
 * Description: singly linked list node struct
 */
typedef struct pyop 
{
	int size;
	int allocated;
	Elements *element;
} PyObject;


/**
 * print_python_list_info - fun to print python list info
 * @p: list opject
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %d\n", p->size);
	printf("[*] Allocated = %d\n", p->allocated);

	for (i = 0; i < p->size; i++)
	{
		if (p->element[i].str != NULL)
			printf("Element %d: %s\n", i, p->element[i].str);
		else 
			printf("Element %d: %d\n", i, p->element[i].inti);
	}
}
