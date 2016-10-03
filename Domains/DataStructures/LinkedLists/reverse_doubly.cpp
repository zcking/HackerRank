/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // If empty list, return
    if (!head) return NULL;

    // Otherwise, swap the next and prev
    Node *temp = head->next;
    head->next = head->prev;
    head->prev = temp;

    // If the prev is now NULL, the list
    // has been fully reversed
    if (!head->prev) return head;

    // Otherwise, keep going
    return Reverse(head->prev);
}
