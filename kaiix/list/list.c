#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

/*
 * doubly linked list
 */

struct list_node {
    int data;
    struct list_node *prev;
    struct list_node *next;
};

void
print_list(struct list_node *header)
{
    struct list_node *ptr = header;
    do {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    } while (ptr != NULL);
    printf("TAIL\n");
}

void
print_list_reverse(struct list_node *list)
{
    while (list->next) {
        list = list->next;
    }

    do {
        printf("%d <- ", list->data);
        list = list->prev;
    } while (list != NULL);
    printf("HEAD\n");
}

struct list_node*
list_new(int data)
{
    struct list_node *node = (struct list_node *)malloc(sizeof(struct list_node));
    node->data = data;
    node->prev = NULL;
    node->next = NULL;
    return node;
}

struct list_node*
list_append(struct list_node *list, int data)
{
    assert(list != NULL);

    struct list_node *tail = list;
    struct list_node *node = list_new(data);
    while (tail->next) {
        tail = tail->next;
    }
    tail->next = node;
    node->prev = tail;
    node->next = NULL;
    return list;
}

struct list_node*
list_prepend(struct list_node *list, int data)
{
    assert(list != NULL);

    struct list_node *node = list_new(data);
    node->prev = list->prev;
    node->next = list;
    if (list->prev) {
        list->prev->next = node;
    }
    list->prev = node;
    return node;
}

struct list_node*
list_insert(struct list_node *list, int position, int data)
{
    assert(list != NULL);

    if (position == 0) {
        return list_prepend(list, data);
    } else if (position < 0) {
        return list_append(list, data);
    }

    struct list_node *tmp = list;
    while ((position-- > 0) && tmp) {
        tmp = tmp->next;
    }

    if (!tmp) {
        list_append(list, data);
    } else {
        struct list_node *node = list_new(data);
        node->prev = tmp->prev;
        node->next = tmp;
        tmp->prev->next = node;
        tmp->prev = node;
    }
    return list;
}

struct list_node*
list_remove(struct list_node *list, int data)
{
    assert(list != NULL);

    struct list_node *tmp = list;

    while (tmp) {
        if (tmp->data == data) {
            if (tmp->prev) {
                tmp->prev->next = tmp->next;
            }
            if (tmp->next) {
                tmp->next->prev = tmp->prev;
            }
            if (list == tmp) {
                list = tmp->next;
            }
            tmp->prev = NULL;
            tmp->next = NULL;
            free(tmp);
            break;
        }
        tmp = tmp->next;
    }

    return list;
}

int main()
{
    struct list_node *list = list_new(3);
    list_append(list, 4);
    list = list_prepend(list, 2);
    list = list_insert(list, 2, 30);
    list = list_insert(list, 3, 31);
    list = list_insert(list, 0, 1);
    list = list_insert(list, 0, 0);
    list = list_insert(list, -1, 5);
    list = list_insert(list, 8, 6);
    list = list_insert(list, 10, 7);
    list = list_insert(list, 999, 70);
    list = list_remove(list, 7);
    list = list_remove(list, 30);
    list = list_remove(list, 31);
    list = list_remove(list, 0);
    list = list_remove(list, 70);
    list = list_remove(list, 70);

    print_list(list);
    print_list_reverse(list);
    return 0;
}

