import java.util.ArrayList;
import java.util.Scanner;
 
public class Solution2 {

    public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       Integer count = scan.nextInt();
       scan.nextLine();
       ArrayList<ArrayList<String>> arr = new ArrayList<ArrayList<String>>();
       
       
    //   for(int i = 0; i <count; i++ ){
    //       String str = scan.nextLine();
           
    //              ArrayList<String> arrayList = new ArrayList<>();
    //     String[] arrOfStr = str.split(" ");
    //           // use add() method to add elements in the arrayList
    //     for (String j : arrOfStr){
    //         arrayList.add(j);
    //     }
    //     arr.add(arrayList);
    //           }
               
               
              Integer count2 = scan.nextInt();
            //   scan.nextLine();
               for(int i = 0; i <count2; i++ ){
           String str = scan.nextLine();
            System.out.println(str);
        String[] arrOfStr = str.split(" ");
        System.out.println(arrOfStr.toString());
            //  int a = Integer.parseInt(arrOfStr[0]); 
               }
               
            //   System.out.println(arr.toString());
       
    }
}