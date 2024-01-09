import java.util.Arrays;

public class Merger {
    public static void main(String[] args) {

        int a[] = {7,8,9,10};
        int b[] = {1,2,3,4,5,6,0,0,0,0};
        // int b[] = new int[10];


        for (int i = 6 ; i<10 ; i++){
           int  j = i;
           b[i] =  a[i-6];
           int temp;
            while(b[j]<b[j-1]){
                temp = b[j-1];  
                b[j-1] = b[j];  
                b[j] = temp;  
            }
        }
        System.out.println(Arrays.toString(b));
    }
}
