using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {
    
    static bool isValid(string exp) {
        Stack<char> s = new Stack<char>();
        
        foreach(char c in exp) {
            if (c == '[' || c == '{' || c == '(') {
                s.Push(c);
                continue;
            }
            
            if (s.Count == 0)
                return false;
            
            char match = s.Pop();
            if ((c == ')' && match != '(') || (c == ']' && match != '[') || (c == '}' && match != '{'))
                return false;
        }
        
        return (s.Count == 0);
    }

    static void Main(String[] args) {
        int t = Convert.ToInt32(Console.ReadLine());
        for(int a0 = 0; a0 < t; a0++){
            string s = Console.ReadLine();
            if (isValid(s))
                Console.WriteLine("YES");
            else
                Console.WriteLine("NO");
        }
    }
}
