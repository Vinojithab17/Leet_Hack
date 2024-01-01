import java.io.*;
import java.util.*;

public class Token {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
   
        Scanner scan = new Scanner(System.in);
        String Input = scan.nextLine();
        String[] tokens = Input.split("[!,?._'@\\s]+");
        System.out.println(tokens.length);
        for (String s : tokens) {
            if(s.length() > 0){
            // System.out.println(s.length());
            System.out.println(s);
                
            }
        }
        scan.close();
    }
}