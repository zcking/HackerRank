/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/
void postOrder(Node root) {
    // Print out left subtree
    if (root.left != null) postOrder(root.left);
    
    // Print out right subtree
    if (root.right != null) postOrder(root.right);
    
    // Print out root
    System.out.print(root.data);
    System.out.print(" ");
}
