import java.io.*;
import java.util.*;


public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        
        
        // Get first half of result
        for (int i=k, j=0; i < n; i++, j++) {
            System.out.print(a[i]);
            System.out.print(" ");
        }
        
        for (int i = 0; i < k; i++) {
            System.out.print(a[i]);
            System.out.print(" ");
        }
    }
}
