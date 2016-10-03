/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node* headA, Node* headB) {
    Node* currentA = headA;
    Node* currentB = headB;

    //Do till the two nodes are the same
    while(currentA != currentB){
        //If you reached the end of one list start at the beginning of the other one
        //currentA
        if(currentA->next == NULL){
            currentA = headB;
        }else{
            currentA = currentA->next;
        }
        //currentB
        if(currentB->next == NULL){
            currentB = headA;
        }else{
            currentB = currentB->next;
        }
    }
    return currentB->data;
}
