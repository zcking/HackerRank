

 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node lca(Node root,int v1,int v2) {
    if (root == null) return null;
    
    // If v1 and v2 are smaller than root, LCA is in left
    if (root.data > v1 && root.data > v2)
        return lca(root.left, v1, v2);
        
    // If both v1 and v2 are greater than root, LCA in in right
    if (root.data < v1 && root.data < v2)
        return lca(root.right, v1, v2);
    
    return root;
}




