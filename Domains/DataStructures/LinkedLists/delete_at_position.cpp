/*
  Delete Node at a given position in a linked list 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
    if (head == NULL)
        return NULL;
    
    if (position == 0) { return head->next; }
    
    int pos = 0;
    Node* cursor = head;
    while (pos < position - 1 && cursor->next != NULL) {
        cursor = cursor->next;
        pos++;
    }
    
    Node* targetNode = cursor->next;
    cursor->next = targetNode->next;
    targetNode->next = NULL;
    
    return head;
}
