/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/

// Reverses a linked list
Node* Reverse(Node *head)
{
    if (head == NULL || head->next == NULL) return head;
    
    Node* n = Reverse(head->next); 
    head->next->next = head; 
    head->next = NULL;
    return n;
}


int GetNode(Node *head,int positionFromTail)
{
    Node* reversed = Reverse(head);
    for (int i = 0; i < positionFromTail; i++) {
        reversed = reversed->next;
    }
    
    return reversed->data;
}
