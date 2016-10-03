
void Print(Node *head)
{
    while (head != NULL) {
        std::cout << head->data << "\n";
        head = head->next;
    }
}
