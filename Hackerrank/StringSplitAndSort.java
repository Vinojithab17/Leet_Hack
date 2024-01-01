import java.util.Arrays;

public class StringSplitAndSort {
    public static void main(String[] args) {
        // Example string of numbers separated by commas
        String a = "528163";
        String b = "123586";

        String aa = a.toLowerCase();
        String bb = b.toLowerCase();
        // Step 1: Split the string
        String[] A = aa.split("");
        String[] B= bb.split("");

        // Step 2 and 3: Convert to integers and store in an array
        // int[] numbers = new int[numberStrings.length];
        // for (int i = 0; i < numberStrings.length; i++) {
        //     numbers[i] = Integer.parseInt(numberStrings[i]);
        // }

        // Step 4: Sort the array
        java.util.Arrays.sort(A);
        java.util.Arrays.sort(B);
        boolean arraysEqual = Arrays.equals(A, B);
        // Display the sorted array
        // return arraysEqual;
    }
}
