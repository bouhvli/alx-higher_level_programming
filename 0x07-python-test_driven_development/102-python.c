#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    const char *type = NULL, *value = NULL;
    Py_ssize_t len = 0;
    PyUnicodeObject *uniCodeObj = NULL;

    printf("[.] string object info\n");
    if (PyUnicode_Check(p))
    {
        uniCodeObj = (PyUnicodeObject *)p;
        type = (PyUnicode_KIND(p) == PyUnicode_1BYTE_KIND ? "compact ascii" : "compact unicode object");
        len = PyUnicode_GET_LENGTH(p);
        value = PyUnicode_AsUTF8(p);
        printf("  type: %s\n", type);
        printf("  length: %ld\n", len);
        printf("  value : %s\n", value);
    }
    else
        printf("  [ERROR] Invalid String Object\n");
}