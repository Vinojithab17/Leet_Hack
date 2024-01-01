import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

 
public class Test {

    public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       Integer count = scan.nextInt();
       scan.nextLine();
       ArrayList<ArrayList<String>> arr = new ArrayList<ArrayList<String>>();
       
       
      for(int i = 0; i <count; i++ ){
          String str = scan.nextLine();
           
                 ArrayList<String> arrayList = new ArrayList<>();
        String[] arrOfStr = str.split(" ");
              // use add() method to add elements in the arrayList
        for (String j : arrOfStr){
            arrayList.add(j);
        }
        arrayList.remove(0);
        arr.add(arrayList);
              }
               
          System.out.println(Arrays.toString(arr.toArray())); 
          
          
              Integer count2 = scan.nextInt();
          System.out.println(count2); 

              scan.nextLine();
               for(int i = 0; i <count2; i++ ){
           String str = scan.nextLine();
            // System.out.println(str);
        String[] arrOfStr = str.split(" ");
        // System.out.println(Arrays.toString(arrOfStr));
             int a = Integer.parseInt(arrOfStr[0]); 

             int b = Integer.parseInt(arrOfStr[1]);
             try {
                        System.out.println(arr.get(a-1).get(b-1));

             } catch(IndexOutOfBoundsException e) {
                System.out.println("Error!");

             }

               }
               
            //   System.out.println(Arrays.toString(arr));
       scan.close();
    }
}