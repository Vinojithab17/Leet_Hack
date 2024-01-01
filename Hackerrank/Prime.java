import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Prime {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        Integer n = scan.nextInt();
        scan.nextLine();
        String S = scan.nextLine();
        
        String[] array = S.split(" ");
        List<String> al = new ArrayList<>(Arrays.asList(array));

        // System.out.println(al.toString());

        Integer n2 = scan.nextInt();
        scan.nextLine();
        for(int i = 0; i < n2; i++){
            String action = scan.nextLine();
            int index = scan.nextInt();
                if(action.equalsIgnoreCase("Insert")){
                    // scan.nextLine();
                            int b = scan.nextInt();


                    al.add(index, String.valueOf(b));
                            // System.out.println(al.toString());

                }
                else{
                   
                    al.remove(index);
        // System.out.println(al.toString());

                }
                try{
                    scan.nextLine();
                }
                catch(Exception e){
                    
                }
          
        }

        System.out.println(al.toString());
  
    for(String s : al){
        System.out.print(s + " ");
    }
        // System.out.println(al.toString()

        
    }
}