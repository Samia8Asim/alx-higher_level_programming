#include <stdio.h>
#include <stdlib.h>

typedef struct {
	char *str;
	int inti;
} Elements;
typedef struct {
	int size;
	int allocated;
	Elements *element;
} PyObject;

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
