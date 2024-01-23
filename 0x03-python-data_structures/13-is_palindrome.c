#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *next = *head;
    listint_t *prev = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (next != NULL && next->next != NULL)
    {
        next = next->next->next;
        prev = current;
        current = current->next;
    }

    if (next != NULL)
    {
        prev = current;
        current = current->next;
    }

    prev->next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    while (*head != NULL && prev != NULL)
    {
        if ((*head)->n != prev->n)
            return (0);
        *head = (*head)->next;
        prev = prev->next;
    }

    return (1);
}
