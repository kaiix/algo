#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct llist_node {
    int data;
    struct llist_node *next;
};

struct llist_node*
new_node(int data)
{
    struct llist_node *node = (struct llist_node *)malloc(sizeof(struct llist_node));
    node->data = data;
    node->next = NULL;
    return node;
}

struct llist_node*
new_llist(int data)
{
    return new_node(data);
}

void
append_node(struct llist_node *llist, int data)
{
    // new node
    struct llist_node *node = (struct llist_node *)malloc(sizeof(struct llist_node));
    node->data = data;
    node->next = NULL;

    // find tail
    struct llist_node *tail = llist;
    while (tail->next != NULL) {
        tail = tail->next;
    }

    // append node
    tail->next = node;
}

void
print_llist(struct llist_node *header)
{
    struct llist_node *ptr = header;
    do {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    } while (ptr != NULL);
    printf("NIL\n");
}

/*
 * return 0 if pos > llist size
 */
int
insert_node(struct llist_node **header, int pos, int data)
{
    assert(pos >= 0);

    if (pos == 0) {
        struct llist_node *node = new_node(data);
        node->next = *header;
        *header = node;
        return 1;
    }

    struct llist_node *prev = *header;
    for (int i = 0; i < pos - 1; i++) {
        prev = prev->next;
        if (prev == NULL) {
            return 0;
        }
    }

    struct llist_node *node = new_node(data);
    struct llist_node *next = prev->next;
    prev->next = node;
    node->next = next;
    return 1;
}

int
remove_node(struct llist_node **header, int pos) {
    assert(pos >= 0);

    if (pos == 0) {
        struct llist_node *ptr = *header;
        *header = (*header)->next;
        free(ptr);
        return 1;
    }

    struct llist_node *prev = *header;
    for (int i = 0; i < pos - 1; i++) {
        prev = prev->next;
        if (prev == NULL) {
            return 0;
        }
    }

    struct llist_node *node_to_delete = prev->next;
    if (node_to_delete == NULL) {
        return 0;
    }
    struct llist_node *next = node_to_delete->next;
    prev->next = next;
    free(node_to_delete);
    return 0;
}

int main()
{
    while (NULL) {
        printf("NULL");
    }

    struct llist_node *llist = new_llist(5);
    append_node(llist, 6);
    append_node(llist, 7);
    print_llist(llist);

    insert_node(&llist, 0, 4);
    insert_node(&llist, 4, 8);
    print_llist(llist);

    remove_node(&llist, 0);
    remove_node(&llist, 3);
    remove_node(&llist, 3);
    print_llist(llist);

    return 0;
}
