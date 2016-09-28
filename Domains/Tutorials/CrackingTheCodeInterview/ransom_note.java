import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        String magazine[] = new String[m];
        for(int magazine_i=0; magazine_i < m; magazine_i++){
            magazine[magazine_i] = in.next();
        }
        String ransom[] = new String[n];
        for(int ransom_i=0; ransom_i < n; ransom_i++){
            ransom[ransom_i] = in.next();
        }
        
        // Quick check
        if (n > m) {
            System.out.println("No");
            return;
        }
        
        boolean failed;
        
        // Go through the note array and use the string from the magazine array
        for (int i = 0; i < n; i++) {
            String note_word = ransom[i];
            failed = true;
            
            for (int j = 0; j < m; j++) {
                String mag_word = magazine[j];
                if (mag_word.compareTo("") == 0)
                    continue;
                
                if (note_word.compareTo(mag_word) == 0) {
                    magazine[j] = "";
                    failed = false;
                    break;
                }
            }
            
            if (failed) {
                System.out.println("No");
                return;
            }
        }
        
        System.out.println("Yes");
    }
}
