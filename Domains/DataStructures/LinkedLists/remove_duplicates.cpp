/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node* head) {
    if ( head == NULL ) return head;
    
    Node* nextItem = head->next;
    
    while (nextItem != NULL && head->data == nextItem->data) {
        nextItem = nextItem->next;
    }
    
    head->next = RemoveDuplicates(nextItem);
    return head;
}
