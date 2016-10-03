/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/

void inOrder(Node root) {
    // Print left subtree
    if (root.left != null) inOrder(root.left);
    
    // Print the root
    System.out.print(root.data);
    System.out.print(" ");
    
    // Print right subtree
    if (root.right != null) inOrder(root.right);
}
