#include <Python.h>
#include <stdio.h>
/**
 * print_python_string - a function that prints Python strings.
 * @p: py object (the string)
*/
void print_python_string(PyObject *p)
{
	const char *type = NULL, *value = NULL;
	Py_ssize_t len = 0;
	PyUnicodeObject *uniCodeObj = NULL;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		uniCodeObj = (PyUnicodeObject *)p;
		if (PyUnicode_KIND(p) == PyUnicode_1BYTE_KIND)
			type = "compact ascii";
		else
			type = "compact unicode object";
		len = PyUnicode_GET_LENGTH(p);
		value = PyUnicode_AsUTF8(p);
		printf("  type: %s\n", type);
		printf("  length: %ld\n", len);
		printf("  value : %s\n", value);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
