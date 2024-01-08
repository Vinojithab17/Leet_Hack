import java.io.Serializable;

public record Person(String name, int age) implements Serializable {
    // Additional custom method
    public String greet() {
        return "Hello, my name is " + name + " and I am " + age + " years old.";
    }

    // Customizing toString() method
    @Override
    public String toString() {
        return "Person: " + name + ", Age: " + age;
    }
}
