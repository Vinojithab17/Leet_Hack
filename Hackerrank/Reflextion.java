import java.lang.reflect.Field;
import java.lang.reflect.Method;

class Cat {

    private final String name;
    private String id;

    public Cat(String name, String id) {
        this.name = name;
        this.id = id;
    }

    public String getname() {
        return this.name;
    }

    public String getid() {
        return this.id;
    }

}

public class Reflextion {

    public static void main(String[] args) {
        Cat newCat = new Cat("Tom", "123");
                    System.out.println(newCat.getname());

        Field[] catFields = newCat.getClass().getDeclaredFields();

        for (Field field : catFields) {
            // System.out.println(field.getName());

            if (field.getName().equals("name")) {
                field.setAccessible(true);
                try {
                    // System.out.println(field.get(newCat));
                    field.set(newCat, "Jerry");
                    // System.out.println(field.get(newCat));
                } catch (IllegalArgumentException | IllegalAccessException e) {
                    e.printStackTrace();
                }
            }

        }
            System.out.println(newCat.getname());


            Method[] catMethods = newCat.getClass().getDeclaredMethods();

            for(Method method : catMethods){
                System.out.println(method.getName());
            }
    }
}
