
public class Num {
    public static void main(String[] args) {
        String s = "hello there";
        System.out.println(s);
        int a = 1;
        int b = 1;
        int c = a++; // Assigns the value and increments
        int d = ++b; // increment and assigns the value
        System.out.println("The Value of c is = " + c);
        System.out.println("The Value of d is = " + d);
        int num = 1;
        System.out.println(++num);
        System.out.println(num++);
        // The Value of c is = 1
        // The Value of d is = 2

    }
}