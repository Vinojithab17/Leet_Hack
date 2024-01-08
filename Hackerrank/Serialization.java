import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Serialization
 */
class Serialization {

    public static void main(String[] args) {
        var p = new Person("John", 25);
        var p2 = new Person("carter", 27);

        List<Person> persons = new ArrayList<Person>(List.of(p, p2));
        System.out.println(persons);
        try {
            // Serialization
            FileOutputStream fos = new FileOutputStream("Serialization.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(persons);
            oos.close();

            // Deserialization
            FileInputStream fis = new FileInputStream("Serialization.txt");
            ObjectInputStream ois = new ObjectInputStream(fis);
            @SuppressWarnings("unchecked")
            ArrayList<Person> person = (ArrayList<Person>) ois.readObject();
            ois.close();

            System.out.println("Deserialized data from Serialization.txt");
            System.out.println(person.get(0));
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }

        // System.out.println(p.age());
    }
}
