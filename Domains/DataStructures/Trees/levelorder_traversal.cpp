#include <queue>


/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

void LevelOrder(node * root)
{
    // Terminal case
    if (root == NULL) return;
    
    queue<node *> q;
    
    q.push(root); // enqueue root
    
    while (!q.empty()) {
        node* n = q.front();
        std::cout << n->data << " ";
        q.pop();
        
        if (n->left != NULL)
            q.push(n->left);
        
        if (n->right != NULL)
            q.push(n->right);
    }
}
