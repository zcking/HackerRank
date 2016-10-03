/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
    // Instantiate new node and set data
    Node* new_node = new Node();
    new_node->data = data;
    
    if (head == NULL) { return new_node; }
    if (position == 0) { new_node->next = head; return new_node; }
    
    int pos = 0;
    Node* cursor = head;
    while (pos < position - 1 && cursor->next != NULL) {
        cursor = cursor->next;
        pos++;
    }
    
    Node* n = cursor->next;
    cursor->next = new_node;
    cursor = cursor->next;
    cursor->next = n;
    
    return head;
}

