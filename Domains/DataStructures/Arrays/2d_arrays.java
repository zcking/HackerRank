import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int arr_i=0; arr_i < 6; arr_i++){
            for(int arr_j=0; arr_j < 6; arr_j++){
                arr[arr_i][arr_j] = in.nextInt();
            }
        }
        
        int max = Integer.MIN_VALUE;
        
        for (int row = 0; row <= 3; row++) {
            for (int col = 0; col <= 3; col++) {
                int top = arr[row][col] + arr[row][col+1] + arr[row][col+2];
                int bot = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2];
                int sum = top + bot + arr[row+1][col+1];
                if (sum > max)
                    max = sum;
            }
        }
        
        System.out.println(max);
    }
}
