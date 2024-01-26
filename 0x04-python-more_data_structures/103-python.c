#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

/**
 * print_python_list - print information about Python lists
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
Py_ssize_t i, size;

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", PyList_GET_SIZE(p));
for (i = 0; i < size; i++)
{
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
}
}

/**
 * print_python_bytes - print information about Python bytes
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t i, size;

size = PyBytes_Size(p);
printf("[*] Python string object info\n");
printf("[*] Size of the Python String = %ld\n", size);
printf("[*] Allocated = %ld\n", PyBytes_GET_SIZE(p));
printf("[*] Value: %s\n", PyBytes_AS_STRING(p));
}
