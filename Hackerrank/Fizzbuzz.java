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

        public void area() {
                String s = String.format("%d %d", this.length, this.width);
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

class Fizzbuzz {
        public static void main(String args[]) {

                System.out.println("Hello World");
                Shape s = new Rectangle(2, 3);
                s.Greet();

                System.out.println(s instanceof Rectangle);
                Rectangle s2 = new Rectangle(2, 3);
                s2.Greet();
        }
}