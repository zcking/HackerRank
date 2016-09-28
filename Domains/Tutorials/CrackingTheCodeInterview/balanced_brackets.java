import java.io.*;
import java.util.*;

public class Solution {
     public static boolean isBalanced(String expression) {
         if (expression.length() % 2 == 1)
            return false;
            
         Stack<Character> s = new Stack<Character>();
         for (char bracket : expression.toCharArray()) {
             
             // Open or closed bracket?
             if (bracket == '{' || bracket == '[' || bracket == '(') {
                 s.push(bracket);
             } else {
                 // Get top bracket and validate
                 if (s.empty())
                     return false;
                 
                 char top = (char)s.pop();

                 boolean valid = ((top == '{' && bracket == '}') || 
                                  (top == '[' && bracket == ']') || 
                                  (top == '(' && bracket == ')'));

                 if (!valid)
                     return false;
             }
         }
         
         return s.empty();
     }
  
   public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
             boolean answer = isBalanced(expression);
             if(answer)
              System.out.println("YES");
             else System.out.println("NO");
        }
       in.close();
    }
}
