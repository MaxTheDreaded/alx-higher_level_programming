#include <stdio.h>
#include <stdlib.h>

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
char *str;

size = PyBytes_Size(p);
str = PyBytes_AsString(p);
printf("[*] Python string object information\n");
printf("[*] String type: %s\n", Py_TYPE(p)->tp_name);
printf("[*] String length: %ld\n", size);
printf("[*] String contains: %s\n", str);
}

/**
 * print_python_float - print information about Python floats
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
printf("[*] Python float object information\n");
printf("[*] Float value: %f\n", PyFloat_AsDouble(p));
}
