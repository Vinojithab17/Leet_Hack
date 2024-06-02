import java.util.ArrayList;
import java.util.List;

/**
 * InnerCasting
 */
class Animal{
    public void eat(){
        System.out.println("Animal is eating");
    }
    private void drink(){
        System.out.println("Animal is drinking");
    }
}

class Dog extends Animal{
    int count = 0;
    // @Override
    // public void eat(){
    //     System.out.println("Dog is eating");
    // }
    public void bark(){
        System.out.println("Dog is barking");
    }
}
public class Casting {
     public static void main(String[] args) {

        List<Animal> animals = new ArrayList<Animal>();
        Animal a = new Dog();   
        Animal a1 = new Animal();
        // Dog d = new Dog();
        // animals.add(d);
        a.eat();

        Dog d = (Dog) a;    
        d.bark();

        // Dog d1 = (Dog) a1;
        // a.coub
        System.out.println(a instanceof Animal);
        System.out.println(a instanceof Dog);

    }
}
