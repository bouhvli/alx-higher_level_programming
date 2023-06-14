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
	Py_ssize_t length, idx;
	PyObject *element;
	PyListObject *lp = (PyListObject *)p;
	const char *tpNAme;

	length = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", length);
	printf("[*] Allocated = %zd\n", lp->allocated);
	for (idx = 0; idx < length; idx++)
	{
		element = lp->ob_item[idx];
		tpNAme = (element)->ob_type->tp_name;
		printf("Element %zd: %s\n", idx, tpNAme);
	}
}
/**
 * print_python_bytes - as the name says.
 * @p: the py object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t length, idx;
	char *string;

	if (PyBytes_Check(p))
	{
		PyBytes_AsStringAndSize(p, &string, &length);
		printf("[.] bytes object info\n");
		printf("  size: %zd\n", length);
		printf("  trying string: %s\n", string);
		if (length < 10)
			printf("  first %zd bytes:", length + 1);
		else
			printf("  first 10 bytes:");
		for (idx = 0; idx < length && idx < 10; idx++)
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
