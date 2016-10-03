import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        int n, d;
        Scanner scan = new Scanner(System.in);
        
        n = scan.nextInt();
        d = scan.nextInt();
        
        int[] arr = new int[n];
        
        // Read in the numbers into the array
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        
        // "Rotate" the array (really, just output the rotation)
        for (int i = d; i < n; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        
        for (int i = 0; i < d; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
    }
}