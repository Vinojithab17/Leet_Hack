/**
 * Fizzbuzz
 */
interface Cat {

        public void doSomeThing();
        
}
interface Dog {

        public void doSomeThing();
        
}

class Animal implements Cat, Dog {

        public void doSomeThing() {
                System.out.println("Animal");
        }
        
}