#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check the singly linked list if it has a cycle
 * @list: points the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listsint_t *sl = list, *ft = list;

	if (list == NULL || list->next == NULL)
		return (0);

	sl = list->next;
	ft = list->next->next;

	while (sl && ft && ft->next)
	{
		if (sl == ft)
			return (1);
	}

	return (0);
}
