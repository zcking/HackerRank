/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node* head,int data) {
    Node* new_node = new Node;
    new_node->data = data;
    
    if (head == NULL) return new_node;
    
    if (data <= head->data) {
        new_node->next = head;
        head->prev = new_node;
        return new_node;
    }

    // If insertion point not found, use recursion
    Node* rest = SortedInsert(head->next, data);
    head->next = rest;
    rest->prev = head;
    return head;
}
