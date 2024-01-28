/**
 * Interface
 */
public interface Interface {
    static int i = 0;
    int j = 0;

    public static void print() {
        System.out.println("Hello World");
    }


}

/**
 * InnerInterface
 */
 class InnerInterface implements Interface {

    public static void main(String[] args) {
        Interface.print();
        System.out.println(Interface.i);
        System.out.println(Interface.j);
    }
}