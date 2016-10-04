/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S ,Node root) {
    String decoded = "";
    Node copy = root;
    
    for(char c : S.toCharArray()) {
        if (c == '0' && root.left != null) 
            root = root.left;
        else if (c == '1' && root.right != null)
            root = root.right;
            
        // leaf?
        if (root.left == null && root.right == null) {
            decoded += root.data;
            root = copy;
        }
    }
        
    System.out.println(decoded);
}
