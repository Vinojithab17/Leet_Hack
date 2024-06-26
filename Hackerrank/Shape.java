import java.util.Scanner;

class Shape {
    int length;
    int width;
    int i = 023;

    public void Greet() {
        System.out.println("Hello from Parent");
    }


    public Shape(int length, int width) {
        this.length = length;
        this.width = width;
    }

    private void area(int a) {
        System.out.println("Area of Shape");
    }

    public void area() {
        String s=String.format("%d %d",this.length, this.width); 
        System.out.println(s);
    }
}


class Rectangle extends Shape {
    @Override
    public void Greet() {
        System.out.println("Hello from Child");
    }

    public Rectangle(int length, int width) {
        super(length, width);
    }
    @Override
    public void area() {
        System.out.println(this.length * this.width);
    }
    
}

class Solution {
    public static void main(String args[] ) throws Exception {
       Scanner scanner = new Scanner(System.in);
       String[] input = scanner.nextLine().split(" ");
       int number1 = Integer.parseInt(input[0]);
              int number2 = Integer.parseInt(input[1]);

              Rectangle rectangle = new Rectangle(number1, number2);
              Shape shape = new Shape(number1, number2);
              shape.area();
              rectangle.area();
            //   System.out.println();

    }
}