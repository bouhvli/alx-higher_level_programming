#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_bytes(PyObject *p);
/**
 * print_python_list - print the py list details.
 * @p: the py object
 */
void print_python_list(PyObject *p)
{
	long int length, idx;
	PyObject *element;
	PyListObject *lp = (PyListObject *)p;
	const char *tpNAme;

	length = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", lp->allocated);
	for (idx = 0; idx < length; idx++)
	{
		element = lp->ob_item[idx];
		tpNAme = (element)->ob_type->tp_name;
		printf("Element %li: %s\n", idx, tpNAme);
		if (strcmp(tpNAme, "bytes") == 0)
		{
			print_python_bytes(lp->ob_item[idx]);
		}
	}
}
/**
 * print_python_bytes - as the name says.
 * @p: the py object
*/
void print_python_bytes(PyObject *p)
{
	long int length, idx;
	char *string;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		PyBytes_AsStringAndSize(p, &string, &length);
		printf("  size: %li\n", length);
		printf("  trying string: %s\n", string);
		if (length < 10)
			printf("  first %li bytes:", length + 1);
		else
			printf("  first 10 bytes:");
		for (idx = 0; idx <= length && idx < 10; idx++)
		{
			printf(" %02hhx", string[idx]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
}
