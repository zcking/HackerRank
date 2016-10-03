/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/

// Prints out the contents of the tree
// in preorder traversal
void preOrder(Node root) {
    // Print the root
    System.out.print(root.data);
    System.out.print(" ");
    
    // Print out the left subtree
    if (root.left != null) preOrder(root.left);
    
    // Print out the right subtree
    if (root.right != null) preOrder(root.right);
}
