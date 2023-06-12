#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
/**
 * print_python_list_info - this will print the list info.
 * @p: the python object.
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (i < Py_SIZE(p))
	{
		printf("Element %d: %s\n",
				i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
